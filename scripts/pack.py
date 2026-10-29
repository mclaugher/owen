#!/usr/bin/env python3
"""pack.py — embed a practice folder in a lesson page.

Usage: python3 scripts/pack.py <practice-folder> <lesson.html> <output.html>

Zips the practice folder, base64-encodes the zip, and replaces the
marker comment `<!-- PACK:PRACTICE -->` in the lesson page with a
download block. The button rebuilds the zip from the embedded data,
so it works offline from a file:// URL.

Seed names: a source file named `CLAUDE.md.seed` downloads as
`CLAUDE.md`. The `.seed` suffix keeps files a tool reads by name
inert in this repo; the packer restores the real name.

The zip uses a fixed timestamp, so packing the same folder twice
produces the same page. Exits non-zero when the folder, the page,
or the marker is missing.

Stdlib only.
"""

import base64
import io
import sys
import zipfile
from pathlib import Path

MARKER = "<!-- PACK:PRACTICE -->"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)

BLOCK_TEMPLATE = """<section class="practice-download" id="practice-download">
  <h2>Practice folder</h2>
  <p>Download the practice folder, then unzip it next to your other projects. The button works offline. Download it again for a fresh copy.</p>
  <p><button type="button" id="practice-download-btn">Download __ZIPNAME__</button></p>
  <script>
  (function () {
    var data = "__B64__";
    document.getElementById("practice-download-btn").addEventListener("click", function () {
      var bin = atob(data);
      var bytes = new Uint8Array(bin.length);
      for (var i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
      var url = URL.createObjectURL(new Blob([bytes], { type: "application/zip" }));
      var a = document.createElement("a");
      a.href = url;
      a.download = "__ZIPNAME__";
      document.body.appendChild(a);
      a.click();
      a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
    });
  })();
  </script>
</section>"""


def build_zip(folder: Path) -> bytes:
    files = sorted(p for p in folder.rglob("*") if p.is_file())
    if not files:
        sys.exit(f"pack.py: practice folder is empty: {folder}")
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            rel = p.relative_to(folder)
            name = rel.name[: -len(".seed")] if rel.name.endswith(".seed") else rel.name
            arcname = "/".join((folder.name,) + rel.parts[:-1] + (name,))
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.external_attr = 0o644 << 16
            zf.writestr(info, p.read_bytes(), zipfile.ZIP_DEFLATED)
    return buf.getvalue()


def main() -> None:
    if len(sys.argv) != 4:
        sys.exit("usage: pack.py <practice-folder> <lesson.html> <output.html>")
    folder = Path(sys.argv[1])
    page = Path(sys.argv[2])
    out = Path(sys.argv[3])
    if not folder.is_dir():
        sys.exit(f"pack.py: practice folder not found: {folder}")
    if not page.is_file():
        sys.exit(f"pack.py: lesson page not found: {page}")
    html = page.read_text(encoding="utf-8")
    if MARKER not in html:
        sys.exit(f"pack.py: marker {MARKER} not found in {page}")

    zipname = f"{folder.name}-practice.zip"
    b64 = base64.b64encode(build_zip(folder)).decode("ascii")
    block = BLOCK_TEMPLATE.replace("__ZIPNAME__", zipname).replace("__B64__", b64)
    out.write_text(html.replace(MARKER, block), encoding="utf-8")
    print(f"pack.py: wrote {out} ({zipname}, {len(b64)} base64 chars)")


if __name__ == "__main__":
    main()
