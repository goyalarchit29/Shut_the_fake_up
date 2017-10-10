package com.example.android.hackbvp;

import android.app.Activity;
import android.app.Dialog;
import android.content.Context;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.AsyncTask;
import android.support.design.widget.BottomSheetBehavior;
import android.support.design.widget.BottomSheetDialogFragment;
import android.support.v4.app.FragmentActivity;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.Charset;
import java.util.ArrayList;

import static android.icu.lang.UCharacter.GraphemeClusterBreak.L;
import static java.security.AccessController.getContext;

public class MainActivity extends FragmentActivity {
    private RecyclerView mRecyclerView;
    private RecyclerView.Adapter mAdapter;
    private RecyclerView.LayoutManager mLayoutManager;
    private static String LOG_TAG = "MainActivity";
    private Button relButton;
    private Button irelButton;
    private int id=-1;
    //public static ArrayList results = new ArrayList<DataObject>();
    //public static BottomSheetBehavior mBottomSheetBehavior1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        new MainActivity.SendDeviceDetails().execute("https://ae24c3f0.ngrok.io/interact/news_item/","Heya!! there");

        mRecyclerView = (RecyclerView) findViewById(R.id.my_recycler_view);
        mRecyclerView.setHasFixedSize(true);
        mLayoutManager = new LinearLayoutManager(this);
        mRecyclerView.setLayoutManager(mLayoutManager);
    }

    @Override
    protected void onResume() {
        super.onResume();
        /*((MyRecyclerViewAdapter) mAdapter).setOnItemClickListener(new MyRecyclerViewAdapter
                .MyClickListener() {

            @Override
            public void onItemClick(final int position, View v) {
                Log.i(LOG_TAG, " Clicked on Item " + position);
                /*relButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {

                        Log.i("Archit","clicked on relevant button of:"+position);
                        final Dialog fbDialogue = new Dialog(MainActivity.this,android.R.style.Theme_Black_NoTitleBar);
                        fbDialogue.getWindow().setBackgroundDrawable(new ColorDrawable(Color.argb(100, 0, 0, 0)));
                        fbDialogue.setContentView(R.layout.dialogue);
                        fbDialogue.setCancelable(true);
                        fbDialogue.show();
                    }
                });

                irelButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View view) {
                        Log.i("Archit","clicked on Irrelevant button of:"+position);
                        final Dialog fbDialogue = new Dialog(MainActivity.this,android.R.style.Theme_Black_NoTitleBar);
                        fbDialogue.getWindow().setBackgroundDrawable(new ColorDrawable(Color.argb(100, 0, 0, 0)));
                        fbDialogue.setContentView(R.layout.dialogue);
                        fbDialogue.setCancelable(true);
                        fbDialogue.show();
                    }
                });
            }



        }); */
    }

    /*private ArrayList<DataObject> getDataSet() {
        ArrayList results = new ArrayList<DataObject>();
        for (int index = 0; index < 20; index++) {
            DataObject obj = new DataObject("Some Primary Text " + index,
                    "Secondary " + index);
            results.add(index, obj);
        }
        return results;
    }*/

    /*public static void openDialogue(){
        final Dialog dialog = new Dialog()
        dialog.setContentView(R.layout.dialogue);
        dialog.setTitle("Title...");

        // set the custom dialog components - text, image and button
        TextView text = (TextView) dialog.findViewById(R.id.text1);
        //text.setText("Android custom dialog example!");
        dialog.show();
    }*/

    private class SendDeviceDetails extends AsyncTask<String, Void, ArrayList<DataObject>> {

        @Override
        protected ArrayList<DataObject> doInBackground(String... params) {

            String jsonResponse = "";

            HttpURLConnection httpURLConnection = null;
            InputStream inputStream = null;
            try {

                httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
                httpURLConnection.setReadTimeout(10000 /* milliseconds */);
                httpURLConnection.setConnectTimeout(15000 /* milliseconds */);
                httpURLConnection.setRequestMethod("GET");
                httpURLConnection.connect();

                if (httpURLConnection.getResponseCode() == 200) {
                    inputStream = httpURLConnection.getInputStream();
                    jsonResponse = readFromStream(inputStream);
                } else {
                    Log.e(LOG_TAG, "Error response code: " + httpURLConnection.getResponseCode());
                }
            } catch (IOException e) {
                Log.e(LOG_TAG, "Problem retrieving the earthquake JSON results.", e);
            } finally {
                if (httpURLConnection != null) {
                    httpURLConnection.disconnect();
                }
                if (inputStream != null) {
                    try {
                        inputStream.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }

            ArrayList<DataObject> results = extractFeatureFromJson(jsonResponse);
            return results;
        }

        @Override
        protected void onPostExecute(ArrayList<DataObject> result) {
            super.onPostExecute(result);
            Log.e("ARCHIT", result.toString());
            mAdapter = new MyRecyclerViewAdapter(MainActivity.this,result);
            mRecyclerView.setAdapter(mAdapter);// this is expecting a response code to be sent from your server upon receiving the POST data
        }
    }

        private String readFromStream(InputStream inputStream) throws IOException {
            StringBuilder output = new StringBuilder();
            if (inputStream != null) {
                InputStreamReader inputStreamReader = new InputStreamReader(inputStream, Charset.forName("UTF-8"));
                BufferedReader reader = new BufferedReader(inputStreamReader);
                String line = reader.readLine();
                while (line != null) {
                    output.append(line);
                    line = reader.readLine();
                }
            }
            return output.toString();
        }

        private ArrayList<DataObject> extractFeatureFromJson(String earthquakeJSON) {
            // If the JSON string is empty or null, then return early.
            if (TextUtils.isEmpty(earthquakeJSON)) {
                return null;
            }

            try {
                JSONObject baseJsonResponse = new JSONObject(earthquakeJSON);
                JSONArray baseArray = baseJsonResponse.getJSONArray("news_items");
                ArrayList results = new ArrayList<DataObject>();
                int size = baseArray.length();
                for (int i = 0; i < size; i++) {
                    JSONObject news = baseArray.getJSONObject(i);
                    String heading = news.getString("heading");
                    String passage = news.getString("passage");
                    String author = news.getString("author");
                    String website = news.getString("website");
                    String image_link = news.getString("image_link");
                    String id=news.getString("id");

                    URL url = null;
                    try {
                        url = new URL(image_link);
                    } catch (MalformedURLException exception) {
                        Log.e(LOG_TAG, "Error with creating URL", exception);
                    }



                    Log.v("heading", heading);
                    Log.v("passage", passage);
                    //Log.v("heading",heading);
                    //Log.v("heading",heading);
                    //Log.v("heading",heading);

                    DataObject obj = new DataObject(heading, passage,image_link,id);
                    Log.d("obj", obj.toString());
                    results.add(obj);

                }
                return results;

            } catch (JSONException e) {
                Log.e(LOG_TAG, "Problem parsing the earthquake JSON results", e);
            }
            return null;
        }
}
