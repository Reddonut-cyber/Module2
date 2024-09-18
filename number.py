name_studen = input("name: " )
point  = float(input("point: "))
if point >= 80:
    print(name_studen, "grade: A", "ดีมากเก่งมาก")
elif point >= 70:
    print(name_studen, "grade: B", "ใช้ได้นะเนี่ย")
elif point >= 60:
    print(name_studen, "grade: C", "โอเคไม่เลว")
elif point >= 50:
    print(name_studen, "grade: D", "ไม่ดีละ สู้!!")
else :
    print(name_studen, "grade: F", "ว๊ายๆๆๆ ไม่ผ่านนนนน")
