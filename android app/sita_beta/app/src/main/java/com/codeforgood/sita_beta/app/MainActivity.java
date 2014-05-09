package com.codeforgood.sita_beta.app;
import android.content.Context;
import android.content.Intent;
import android.content.IntentSender;
import android.location.Location;
import android.os.Bundle;
import android.support.v4.app.FragmentActivity;
import android.util.Log;
import android.view.View;
import android.location.Address;
import android.location.Geocoder;
import android.widget.Toast;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.GooglePlayServicesClient;
import com.google.android.gms.common.GooglePlayServicesUtil;
import com.google.android.gms.location.LocationClient;
import com.google.android.gms.maps.CameraUpdate;
import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.GoogleMap;
import com.google.android.gms.maps.MapFragment;
import com.google.android.gms.maps.SupportMapFragment;
import com.google.android.gms.maps.model.BitmapDescriptorFactory;
import com.google.android.gms.maps.model.CameraPosition;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.Marker;
import com.google.android.gms.maps.model.MarkerOptions;

import java.io.IOException;
import java.util.Locale;

public class MainActivity extends FragmentActivity implements
        GooglePlayServicesClient.ConnectionCallbacks,
        GooglePlayServicesClient.OnConnectionFailedListener, GoogleMap.OnMapClickListener, GoogleMap.OnMarkerClickListener {

    private final static int CONNECTION_FAILURE_RESOLUTION_REQUEST = 9000;

    private LocationClient mLocationClient;
    private Location mCurrentLocation;
    private GoogleMap map;
    private Marker marker = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setUpMapIfNeeded();
        map.setOnMapClickListener(new GoogleMap.OnMapClickListener() {
            @Override
            public void onMapClick(LatLng point) {
                clearMarkers();

                marker = map.addMarker(new MarkerOptions().position(point).title(point.toString()).snippet("Test"));


            }

        });
        map.setOnMarkerClickListener(new GoogleMap.OnMarkerClickListener() {
            @Override
            public boolean onMarkerClick(Marker m) {

                return false;
            }
        });
    }

    private void clearMarkers() {
        Log.i("INFO", "clearing all markers in the map");
        map.clear();
    }


    @Override
    protected void onResume() {
        super.onResume();
        setUpMapIfNeeded();
        setUpLocationClientIfNeeded();
        mLocationClient.connect();
    }

    private void setUpMapIfNeeded() {
        // Do a null check to confirm that we have not already instantiated the
        // map.
        if (map == null) {
            // Try to obtain the map from the SupportMapFragment.
            try {
//                map = ((SupportMapFragment) getSupportFragmentManager()
//                        .findFragmentById(R.id.map)).getMap();
                map = ((MapFragment) getFragmentManager().findFragmentById(R.id.map)).getMap();

            } catch (NullPointerException e) {
                Log.e("ERROR", "NO MAP data");
            }
            // Check if we were successful in obtaining the map.
            if (map == null) {
                Toast.makeText(this, "Google maps not available",
                        Toast.LENGTH_LONG).show();
            }
        }
    }

    private void setUpLocationClientIfNeeded() {
        if (mLocationClient == null) {
            Toast.makeText(getApplicationContext(), "Waiting for location",
                    Toast.LENGTH_SHORT).show();
            mLocationClient = new LocationClient(getApplicationContext(), this, // ConnectionCallbacks
                    this); // OnConnectionFailedListener
        }
    }

    @Override
    public void onPause() {
        super.onPause();
        if (mLocationClient != null) {
            mLocationClient.disconnect();
        }
    }

    /*
     * Called by Location Services when the request to connect the client
     * finishes successfully. At this point, you can request the current
     * location or start periodic updates
     */
    @Override
    public void onConnected(Bundle dataBundle) {
        mCurrentLocation = mLocationClient.getLastLocation();
        if (mCurrentLocation != null) {
            Toast.makeText(getApplicationContext(), "Found!",
                    Toast.LENGTH_SHORT).show();
            centerInLoc();
        }
    }

    private void centerInLoc() {
        LatLng myLaLn = new LatLng(mCurrentLocation.getLatitude(),
                mCurrentLocation.getLongitude());
        CameraPosition camPos = new CameraPosition.Builder().target(myLaLn).zoom(15).bearing(45).tilt(70).build();
        CameraUpdate camUpd3 = CameraUpdateFactory.newCameraPosition(camPos);
        map.animateCamera(camUpd3);

        MarkerOptions markerOpts = new MarkerOptions().position(myLaLn).title(
                "my Location");
        map.addMarker(markerOpts);
    }

    /*
     * Called by Location Services if the connection to the location client
     * drops because of an error.
     */
    @Override
    public void onDisconnected() {
        // Display the connection status
        Toast.makeText(this, "Disconnected. Please re-connect.",
                Toast.LENGTH_SHORT).show();
    }

    /*
     * Called by Location Services if the attempt to Location Services fails.
     */
    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {
        /*
         * Google Play services can resolve some errors it detects. If the error
         * has a resolution, try sending an Intent to start a Google Play
         * services activity that can resolve error.
         */
        if (connectionResult.hasResolution()) {
            try {
                // Start an Activity that tries to resolve the error
                connectionResult.startResolutionForResult(this,
                        CONNECTION_FAILURE_RESOLUTION_REQUEST);
                /*
                 * Thrown if Google Play services canceled the original
                 * PendingIntent
                 */
            } catch (IntentSender.SendIntentException e) {
                // Log the error
                e.printStackTrace();
            }
        } else {
            /*
             * If no resolution is available
             */
            Log.e("Home", Integer.toString(connectionResult.getErrorCode()));
        }
    }

    public void getMyLocation(View view) {
        clearMarkers();
        LatLng myLatLong = new LatLng(mCurrentLocation.getLatitude(), mCurrentLocation.getLongitude());
        MarkerOptions markerOpts = new MarkerOptions().position(myLatLong).title("my Location");
        map.addMarker(markerOpts);
    }


    @Override
    public void onMapClick(LatLng point) {
        map.addMarker(new MarkerOptions().position(point).title("School Position")
                .icon(BitmapDescriptorFactory.defaultMarker(BitmapDescriptorFactory.HUE_RED)));
        Log.i("INFO", "CHECKING CLICK");

    }


    public void uploadReport(View view) {


    }

    @Override
    public boolean onMarkerClick(Marker marker) {
        return false;
    }
}
