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

def insertDownload(userName,id,date):#向下载表中插入数据，日期为"2022-07-05"类似格式
    cursor = db.cursor();
   
    try:
        sql="SELECT * FROM `test`.`download` WHERE `userName` = '%s' AND `id` = '%s' AND `date` = '%s';"\
            % (userName,id,date)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result==None:
            sql="INSERT INTO `test`.`download` (`userName`, `id`, `date`, `times`) \
                VALUES ('%s', '%s', '%s', '%s');" %\
                (userName,id,date,'1')
            cursor.execute(sql)
            db.commit()
            print("insert download")
        else:
            times=result[3]+1
            sql="UPDATE `test`.`download` SET `times` = '%s' \
                WHERE (`userName` = '%s') and (`id` = '%s') and (`date` = '%s');"\
                % (times,userName,id,date)
            cursor.execute(sql)
            db.commit()
            print("add times")
        return(True)
    except:
        db.rollback()
        print("insert failed:(")
        return(False)

def insertListen(userName,id,date):#向听书表中插入数据
    cursor = db.cursor();
    try:
        sql="SELECT * FROM `test`.`listen` WHERE `userName` = '%s' AND `id` = '%s' AND `date` = '%s';"\
            % (userName,id,date)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result==None:
            sql="INSERT INTO `test`.`listen` (`userName`, `id`, `date`)\
                VALUES ('%s', '%s', '%s');" %\
                (userName,id,date)
            cursor.execute(sql)
            db.commit()
            print("insert listen")
        else:
            print("no change required")
        return(True)
    except:
        db.rollback()
        print("insert failed:(")
        return(False)

def insertUpload(userName,id,date):#向上传表中插入数据
    cursor = db.cursor();
    try:
        sql="SELECT * FROM `test`.`upload` WHERE `userName` = '%s' AND `id` = '%s' AND `date` = '%s';"\
            % (userName,id,date)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result==None:
            sql="INSERT INTO `test`.`upload` (`userName`, `id`, `date`)\
                VALUES ('%s', '%s', '%s');" %\
                (userName,id,date)
            cursor.execute(sql)
            db.commit()
            print("insert upload")
        else:
            print("no change required")
        return(True)
    except:
        db.rollback()
        print("insert failed:(")
        return(False)

def insertResource(id,label,title,name,summary,type):#向资源表中插入数据
    cursor = db.cursor();
    sql="INSERT INTO `test`.`resource` (`id`, `label`, `title`, `name`, `summary`, `type`) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s'); "%\
            (id,label,title,name,summary,type)
    try:
        cursor.execute(sql)
        db.commit()
        print("insert successful:)")
        return(True)
    except:
        db.rollback()
        print("insert failed:(")
        return(False)
