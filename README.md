# Ivory_tower

heroku create bot-test --buildpack heroku/python --region eu

heroku buildpacks:set heroku/python

git push heroku master
heroku ps:scale bot=1
heroku logs --tail
heroku ps:stop bot