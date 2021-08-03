Q3) Is this supervised or unsupervised learning? Why? PDF
    با توجه به کوئری که از دیتا میزنیم ممکن است هر کدام از دو حالت رخ دهد.
    در ادامه سوالات با توجه به اینکه درحال حدس قیمت (برچسب) برحسب ویژگی ها هستیم یک supervised learning داریم



Q5) Write a short description about dataset distribution. PDF
    با توجه به standard deviation و میانگین هر ستون داده  AVG/STD میتوان نظر داد.
symboling           1.492912
wheelbase           0.060976
carlength           0.070884
carwidth            0.032549
carheight           0.045482
curbweight          0.203744
enginesize          0.328135
boreratio           0.081340
stroke              0.096331
compressionratio    0.391622
horsepower          0.379805
peakrpm             0.093068
citympg             0.259408
highwaympg          0.223940
price               0.601719
    مثلا symbolin نسبت پراکندگی به میانگین ضریب بالایی دارد یا weelbase پراکندگی نسبتا کمی دارد.
    همچنین بازه مقادیر هر کدام از این مقادیر بسیار با همدیگر متفاوت است که در صورت نیاز به یادگیری با چند ویژگی باید علاوه بر حذف outlier ها نسبت به نرمال سازی اقدام کنیم . من جهت ایجاد regression با پایپ لاین و StandardScaler این کار را انجام دادم

    
Q11) How much is this model accurate ( Use SKlearn library )? PDF
    با توجه به اینکه قیمت خودرو تنها وابسته به اندازه سایز موتور نیست بنابراین طبیعی است که به صورت 100 درصدی به درستی نتواند حدس بزند 
    حتی اگر با overfitting بتوانیم یک درصد بالایی حدس صحیح بزنیم باز هم در مواجه با دیتا خارج از مجموعه قطعا بع مشکل میخوریم
    در مدل فعلی با توجه به تابع تست رگرشن به حدود 75٪ دقت رسیدیم
