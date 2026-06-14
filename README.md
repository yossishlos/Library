#  Library Management System

---

## 1. תיאור המערכת

#המערכת מאפשרת לשאול ספרים, להחזיר ספרים, בנוסף המערכת מנהלת את חשבונות המנוים כמו להוסיף או להסיר חשבון מנוי
#בנוסף ניתן לעדכן ספרים חדשים כולל הז'אנר ושם הסופר 

## 2. הקוד ליצירת MySQL עם Docker

#כדי להרים את מסד הנתונים במהירות, בסביבה מבודדת ועם הגדרות קבועות מראש, ניתן להשתמש בפקודת ה-Docker הבאה:

```bash
docker run --name my-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=library_db -p 3306:3306 -v mysql_data:/var/lib/mysql -d mysql:latest
```

## 3. מבנה התקיות

```
library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore
```

## 4. מבנה טבלאות

### טבלת books — שדות

```
id \מפתח ראשי
title \כותרת הספר, עמודה לא ריקה, מקסימום 50 תווים
author \שם המחבר, עמודה לא ריקה, מקסימום 50 תווים
genre \ערכי genre מותרים:
        מומש — Fiction | Non-Fiction | Science | History | Other
        כעמודת ENUM במסד הנתונים, כל ערך אחר מחזיר שגיאה,
        עמודה לא ריקה
available_is \האם הספר זמין להשאלה — FALSE מסמן הושאל
עמודה לא ריקה
id_member_by_borrowed \מזהה החבר שמחזיק את הספר 
        — NULL אם  זמין
```

### טבלת members — שדות
```
id \מפתח ראשי
name \שם החבר, עמודה לא ריקה, מקסימום 50 תווים
email \כתובת מייל — ייחודית, עמודה לא ריקה
tive_is \האם החבר פעיל — FALSE לא יכול להשאיל
        עמודה לא ריקה
rrows_total \מונה סה"כ השאלות — עולה ב1- בכל השאלה
            עמודה לא ריקה
```

## 5. Endpoints רשימת 

```
POST /books
GET /books
GET /books/{id}
PUT /books/{id}
PUT
/books/{id}/return/{
member_id}
PUT
/books/{id}/borrow/{
member_id}
mmary/reports/ GET
GET /reports/summary
GET /reports/summary
GET
/reports/books-by-ge
nre
PUT
/books/{id}/borrow/{
member_id}
```

## 6. זרימת המערכת

```
מנהל
        ספרים
                יצירת ספר
                        Endpoint /books
                         המשתמש שולח genre/author/title — המערכת מוסיפה
                        is_available=True, borrowed_by=NULL
                צפיה בכל הספרים
                        Endpoint /books
                        get_all_books()
                מציאת ספר לפי id
                        Endpoint /books/{id}
                        get_book_by_id(id)
                עדכון ספר
                        Endpoint books/{id}
                        update_book(id, data)
                השאלת ספר
                        Endpoint /books/{id}/borrow/{member_id} 
                החזרת ספר
                        Endpoint /books/{id}/borrow/{member_id} 
        חברים
                יצירת חבר
                צפיה בכל החברים
                מציאת חבר לפי id
                עדכון חבר
                השבתת חבר
                הפעלת חבר
        דוחות
                דוח כללי
                צפיה בספרים לפי זאנר
                החבר הכי פעיל

```