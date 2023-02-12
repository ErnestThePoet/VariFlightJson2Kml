# VariFlightJson2Kml
Flight track data exported from the Chinese ADS-B tracker site [VariFlight](https://flightadsb.variflight.com/) are offered in `csv` or `json` formats, without the `kml` option that FlightAware offers and we are familiar with, making it difficult to view the flight track in Google Earth. Since VariFlight has much better ADS-B coverage in China, I feel obliged to write this conversion script.  
Simply place the exported `json` file, modify `INPUT_PATH` and `OUTPUT_PATH` in `convert.py`, and run the script.