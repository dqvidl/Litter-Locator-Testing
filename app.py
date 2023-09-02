import streamlit as st
from geopy.geocoders import Nominatim

# Set the title of the web app
st.title("Address to Coordinates Converter")

# Create a text input for the user to enter an address
user_address = st.text_input("Enter an address:")

# Create a button to trigger the conversion
if st.button("Convert"):
    if user_address:
        # Initialize a geocoder
        geolocator = Nominatim(user_agent="address-to-coordinates-converter")

        try:
            # Attempt to geocode the user's input address
            location = geolocator.geocode(user_address)

            if location:
                # Display the latitude and longitude
                st.success(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
            else:
                st.error("Address not found. Please enter a valid address.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

    else:
        st.warning("Please enter an address to convert.")
