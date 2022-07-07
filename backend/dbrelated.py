def insertUser(userName,phone,email,password,uploadRight,vip,db):#向用户表中插入数据
    cursor = db.cursor();
   
    try:
        sql="SELECT * FROM `test`.`user` \
            WHERE `userName` = '%s' " % (userName)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result==None:
            sql="INSERT INTO `test`.`user` (`userName`, `phone`, `email`, `password`, `uploadRight`, `vip`) \
                VALUES ('%s', '%s', '%s', '%s','%s', '%s');" %\
                (userName,phone,email,password,uploadRight,vip)
            cursor.execute(sql)
            db.commit()
            print("insert user")
        else:
            sql="UPDATE `test`.`user` SET `password` = '%s' , `uploadRight`= '%s', `vip`= '%s'\
                WHERE (`userName` = '%s');"\
                % (password,uploadRight,vip,userName)
            cursor.execute(sql)
            db.commit()
            print("update user")
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

def insertDownload(userName,id,date,db):#向下载表中插入数据，日期为"2022-07-05"类似格式
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
        return True
    except:
        db.rollback()
        print("insert failed:(")
        return False 

def insertListen(userName,id,date,db):#向听书表中插入数据
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
        return True 
    except:
        db.rollback()
        print("insert failed:(")
        return False 

def insertUpload(userName,id,date,db):#向上传表中插入数据
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
        return True 
    except:
        db.rollback()
        print("insert failed:(")
        return False 

def insertResource(id,label,title,name,summary,type,location,db):#向资源表中插入数据
    cursor = db.cursor();
    sql="INSERT INTO `test`.`resource` (`id`, `label`, `title`, `name`, `summary`, `type`, `location`) \
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s'); "%\
            (id,label,title,name,summary,type,location)
    try:
        cursor.execute(sql)
        db.commit()
        print("insert successful:)")
        return True 
    except:
        db.rollback()
        print("insert failed:(")
        return False 

def insertUp(userName,id,upValue,db):#向up表中插入数据，包含更新
    cursor = db.cursor();
   
    try:
        sql="SELECT * FROM `test`.`up` WHERE `userName` = '%s' AND `id` = '%s' ;"\
            % (userName,id)
        cursor.execute(sql)
        result = cursor.fetchone()
        if result==None:
            sql="INSERT INTO `test`.`up` (`userName`, `id`, `upValue`) \
                VALUES ('%s', '%s', '%s');" %\
                (userName,id,upValue)
            cursor.execute(sql)
            db.commit()
            print("insert up")
        else:
            sql="UPDATE `test`.`up` SET `upValue` = '%s' \
                WHERE (`userName` = '%s') and (`id` = '%s');"\
                % (upValue,userName,id)
            cursor.execute(sql)
            db.commit()
            print("update up")
        return True 
    except:
        db.rollback()
        print("insert failed:(")
        return False 

def queryUp(userName,id,db):#查找Up表
    cursor = db.cursor();
    sql="SELECT * FROM `test`.`up` \
       WHERE `userName` = '%s' AND `id` = '%s';"% (userName,id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        if (result[2])==1:
            print("upValue is True")
            return True
        else:
            print("upValue is False")
            return False
    except:
        print ("query failed:)")
        return False

def queryResource(id,db):#查找资源信息表，成功返回全部资源信息，失败返回False
    cursor = db.cursor();
    sql="SELECT * FROM `test`.`resource` \
       WHERE `id` = '%s';" % (id)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except:
        print ("query failed:)")
        return False

def queryRight(userName,db):#返回用户的上传和vip权限（先上传再vip）
    cursor = db.cursor();
    sql="SELECT * FROM `test`.`user` \
       WHERE `userName` = '%s' " % (userName)
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        return (result[4],result[5])
    except:
        print ("query failed:)")
        return False
    
def queryAllResource(userName,db):
    cursor = db.cursor();
    try:
        sql="SELECT * FROM `test`.`upload` \
       WHERE `userName` = '%s' " % (userName)
        cursor.execute(sql)
        result = cursor.fetchall()
        i=0
        list=[]
        try:
            while result[i][1]:
                list.append(queryResource(result[i][1]))
                i=i+1
        except:
            return(list)
    except:
        print ("query failed:)")
        return False
