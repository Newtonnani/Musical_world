Audio file type can be one of the following 1 – Song , 2 – Podcast , 3 – Audiobook

#python version Python 3.8.5

create virtualenv and activate

pip install -r requirements.txt

export SQLALCHEMY_DATABASE_URI=sqlite:///site.db
export FLASK_APP=run.py
export FLASK_ENV=development

python run.py
