package com.example.android.hackbvp;

/**
 * Created by archi on 10-10-2017.
 */

import android.app.Dialog;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.TextView;

import java.util.ArrayList;

public class MyRecyclerViewAdapter extends RecyclerView
        .Adapter<MyRecyclerViewAdapter
        .DataObjectHolder> {
    private static String LOG_TAG = "MyRecyclerViewAdapter";
    private ArrayList<DataObject> mDataset;
    private static MyClickListener myClickListener;

    public static class DataObjectHolder extends RecyclerView.ViewHolder
            implements View
            .OnClickListener {
        TextView label;
        TextView dateTime;

        int clickId=-1;

        public DataObjectHolder(final View itemView) {
            super(itemView);
            label = (TextView) itemView.findViewById(R.id.title);
            dateTime = (TextView) itemView.findViewById(R.id.description);
            relButton=(Button)itemView.findViewById(R.id.rel);
            irelButton=(Button)itemView.findViewById(R.id.irre);
            itemView.setOnClickListener(this);

            relButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    clickId=itemView.getId();
                    Log.i("Archit","clicked on relevant button of:"+clickId);
                    final Dialog fbDialogue = new Dialog(,android.R.style.Theme_Black_NoTitleBar);
                    fbDialogue.getWindow().setBackgroundDrawable(new ColorDrawable(Color.argb(100, 0, 0, 0)));
                    fbDialogue.setContentView(R.layout.dialogue);
                    fbDialogue.setCancelable(true);
                    fbDialogue.show();
                }
            });

            irelButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    clickId=itemView.getId();
                    Log.i("Archit","clicked on Irrelevant button of:"+clickId);
                }
            });

            Log.i(LOG_TAG, "Adding Listener");
            //itemView.setOnClickListener(this)
        }

        @Override
        public void onClick(View v) {
            myClickListener.onItemClick(getAdapterPosition(), v);
        }
    }

    public void setOnItemClickListener(MyClickListener myClickListener) {
        this.myClickListener = myClickListener;
    }

    public MyRecyclerViewAdapter(ArrayList<DataObject> myDataset) {
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
    public void onBindViewHolder(DataObjectHolder holder, int position) {
        holder.label.setText(mDataset.get(position).getmText1());
        holder.dateTime.setText(mDataset.get(position).getmText2());
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

    public interface MyClickListener {
        public void onItemClick(int position, View v);
    }
}