package com.example.android.hackbvp;

/**
 * Created by archi on 10-10-2017.
 */

import android.app.Activity;
import android.app.Dialog;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.AsyncTask;
import android.support.design.widget.BottomSheetBehavior;
import android.support.design.widget.BottomSheetDialogFragment;
import android.support.v4.app.FragmentActivity;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

import static android.R.string.no;
import static android.R.string.yes;
import static com.example.android.hackbvp.R.id.rel;
import static java.lang.System.load;

public class MyRecyclerViewAdapter extends RecyclerView
        .Adapter<MyRecyclerViewAdapter
        .DataObjectHolder> {
    private static String LOG_TAG = "MyRecyclerViewAdapter";
    private ArrayList<DataObject> mDataset;
    private Bitmap bmp=null;
    public Context context;

    public static class DataObjectHolder extends RecyclerView.ViewHolder
             {
        TextView label;
        TextView dateTime;
                 Button relButton;
                 Button irelButton;
         ImageView image;

        public DataObjectHolder(final View itemView) {
            super(itemView);
            label = (TextView) itemView.findViewById(R.id.title);
            dateTime = (TextView) itemView.findViewById(R.id.description);
            image=(ImageView)itemView.findViewById(R.id.thumbnail);
            relButton=(Button)itemView.findViewById(R.id.rel);
            irelButton=(Button)itemView.findViewById(R.id.irre);
        }
    }

    public MyRecyclerViewAdapter(Context c ,ArrayList<DataObject> myDataset) {
        context=c ;
        mDataset = myDataset;
    }

    @Override
    public DataObjectHolder onCreateViewHolder(ViewGroup parent,
                                               int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.activity_card_view, parent, false);

        DataObjectHolder dataObjectHolder = new DataObjectHolder(view);
        return dataObjectHolder;
    }

    @Override
    public void onBindViewHolder(final DataObjectHolder holder, final int position) {

        Log.i("GOY",mDataset.get(position).getmText1());

        holder.label.setText(mDataset.get(position).getmText1());
        holder.dateTime.setText(mDataset.get(position).getmText2());

        Picasso.with(context).load(mDataset.get(position).getmImage()).into(holder.image);

        holder.relButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.i("Archit","clicked on relevant button of:"+position);
                //MainActivity.openDialogue();
                JSONObject jobj=new JSONObject();
                try {
                    jobj.put("id",mDataset.get(position).getmid());
                    jobj.put("type","1");
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                new MyRecyclerViewAdapter.SendDeviceDetails().execute("https://ae24c3f0.ngrok.io/interact/submit/",jobj.toString());
                holder.relButton.setEnabled(false);
                holder.irelButton.setEnabled(false);
            }
        });
        holder.irelButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Log.i("Archit","clicked on relevant button of:"+position);
                //MainActivity.openDialogue();
                JSONObject jobj=new JSONObject();
                try {
                    jobj.put("id",mDataset.get(position).getmid());
                    jobj.put("type","0");
                } catch (JSONException e) {
                    e.printStackTrace();
                }

                new MyRecyclerViewAdapter.SendDeviceDetails().execute("https://ae24c3f0.ngrok.io/interact/submit/",jobj.toString());
                holder.irelButton.setEnabled(false);
                holder.relButton.setEnabled(false);
            }
        });
    }

    public void addItem(DataObject dataObj, int index) {
        mDataset.add(index, dataObj);
        notifyItemInserted(index);
    }

    public void deleteItem(int index) {
        mDataset.remove(index);
        notifyItemRemoved(index);
    }

    @Override
    public int getItemCount() {
        return mDataset.size();
    }

    private class SendDeviceDetails extends AsyncTask<String, Void, String> {

        @Override
        protected String doInBackground(String... params) {

            String data = "";

            HttpURLConnection httpURLConnection = null;
            try {

                httpURLConnection = (HttpURLConnection) new URL(params[0]).openConnection();
                httpURLConnection.setRequestMethod("POST");

                httpURLConnection.setDoOutput(true);

                DataOutputStream wr = new DataOutputStream(httpURLConnection.getOutputStream());
                wr.writeBytes("PostData=" + params[1]);
                wr.flush();
                wr.close();

                InputStream in = httpURLConnection.getInputStream();
                InputStreamReader inputStreamReader = new InputStreamReader(in);

                int inputStreamData = inputStreamReader.read();
                while (inputStreamData != -1) {
                    char current = (char) inputStreamData;
                    inputStreamData = inputStreamReader.read();
                    data += current;
                }
            } catch (Exception e) {
                e.printStackTrace();
            } finally {
                if (httpURLConnection != null) {
                    httpURLConnection.disconnect();
                }
            }

            return data;
        }

        @Override
        protected void onPostExecute(String result) {
            super.onPostExecute(result);
            Log.e("ARCHIT", result);
            String id="";
            String yes="";
            String no="";
            String confidence="";
            try {
                JSONObject jobj=new JSONObject(result);
                id=jobj.getString("id");
                yes=jobj.getString("yes");
                no=jobj.getString("no");
                confidence=jobj.getString("confidence");
            } catch (JSONException e) {
                e.printStackTrace();
            }

            final Dialog dialog = new Dialog(context);
            dialog.setContentView(R.layout.dialogue);
            dialog.setTitle("Title...");

            // set the custom dialog components - text, image and button
            TextView text1 = (TextView) dialog.findViewById(R.id.text1);
            TextView text2 = (TextView) dialog.findViewById(R.id.text2);
            TextView text3 = (TextView) dialog.findViewById(R.id.text3);
            text1.setText(yes+"% Relevant");
            text2.setText(no+"% Irrelevant");
            text3.setText("AI Confidence: "+confidence+"%");
            //text.setText("Android custom dialog example!");

            dialog.getWindow().getAttributes().windowAnimations = R.style.CustomAnimations_slide;
            dialog.getWindow().setBackgroundDrawableResource(android.R.color.transparent);
            dialog.show();
            Window window = dialog.getWindow();

            // this is expecting a response code to be sent from your server upon receiving the POST data
        }
    }

}