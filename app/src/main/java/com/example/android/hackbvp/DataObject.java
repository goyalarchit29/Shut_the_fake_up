package com.example.android.hackbvp;

/**
 * Created by archi on 10-10-2017.
 */

public class DataObject {
    private String mText1;
    private String mText2;
    private String mImage;
    private String mid;
    //private String mText3;

    DataObject (String text1, String text2,String image,String id){
        mText1 = text1;
        mText2 = text2;
        mImage = image;
        mid=id;
        //mText3 = text3;
    }

    public String getmText1() {
        return mText1;
    }

    public void setmText1(String mText1) {
        this.mText1 = mText1;
    }

    public String getmText2() {
        return mText2;
    }

    public void setmText2(String mText2) {
        this.mText2 = mText2;
    }

    //public String getmText3() { return mText3;}

    //public void setmText3(String mText3) {this.mText3=mText3;}

    public void setmImage(String mImage) {
        this.mImage = mImage;
    }

    public String getmImage() {
        return mImage;
    }

    public void setmid(String mid) {
        this.mid = mid;
    }

    public String getmid() {
        return mid;
    }

}