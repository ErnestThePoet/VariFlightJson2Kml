# VariFlightJson2Kml
Flight track data exported from the Chinese ADS-B tracker site [VariFlight](https://flightadsb.variflight.com/) are only offered in `csv` or `json` formats. Absence of direct access to `kml` makes it difficult to visualize flight track in Google Earth. Since VariFlight has much better ADS-B coverage in China, I feel obliged to write this conversion script.  

### Usage
Simply ***drag*** the `json` file(s) onto `convert.bat`. Then you'll see the `kml` output file(s) in the same directory as `json` source file(s).