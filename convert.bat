for %%f in (%*) do (
  python convert.py "%%~ff" "%%~dpf%%~nf.kml"
)