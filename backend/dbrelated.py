def insertUser(userName,phone,email,password,uploadRight,vip,db):#向用户表中插入数据
    cursor = db.cursor();
    sql="INSERT INTO `test`.`user` (`userName`, `phone`, `email`, `password`, `uploadRight`, `vip`) \
     VALUES ('%s', '%s', '%s', '%s','%s', '%s');" %\
        (userName,phone,email,password,uploadRight,vip)
    try:
        cursor.execute(sql)
        db.commit()
        print("insert successful:)")
        return True
    except:
        db.rollback()
        print("insert failed:(")
        return False

def queryUser(userName,password,db):#查找用户信息表
    cursor = db.cursor();
    sql="SELECT * FROM `test`.`user` \
       WHERE `userName` = '%s' " % (userName)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[3])==password:
            print("Correct password")
            return True
        else:
            print("Wrong password")
            return False
    except:
        print ("query failed:)")
        return False

def insertComment(commentId,userName,content,db):#向评论表中插入数据
    cursor = db.cursor();
    sql="INSERT INTO `test`.`comment` (`commentId`, `userName`, `content`) \
     VALUES ('%s', '%s', '%s');" %\
        (commentId,userName,content)
    try:
        cursor.execute(sql)
        db.commit()
        print("insert successful:)")
        return True
    except:
        db.rollback()
        print("insert failed:(")
        return False
