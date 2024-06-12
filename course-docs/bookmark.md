# Module 1: Static Pages

[Coursera Instructions](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-CD0321EN-Coursera/labs/v2/m1/AddStaticPages.md.html)

## Secrets

- Django superuser: root, root@bestcars.com, matt12345625
    - from manage.py createsuperuser
- regular user: matt12345, matt@bestcars.com, matt12345625

## Changelog

- 2.16.2024: Done step 4 on tab 3.
- 2.19.2024: tab 3, see step 9 and 10. May need to do this in Theia.
- 2.22.2024: Got about/ endpoint working.  TODO: style About.html.
- 2.23.2024: Updated about page.  Added start.sh to repo.  TODO: step 5, update contact us page.
- 2.29.2024: week 2.  Step 3
    - in server/frontend:
    - npm install
    - npm run build
    - completed step 5 of week 2.  TODO: complete step 6, logout functionality
- 3.6.2024: week 2, step 6 done.
    - NOTE: updated start.sh.  Not sure if it works yet.
    - TODO: Complete step 6, register functionality.  Needs debugging.  Something with /register vs /registration routes, I believe.
- 3.8.2024: finished week 2.  TODO: begin week 3.
- 6.5.2024: starting module 3.
    - DONE: implement incomplete Express endpoints in server/database/app.js.  (Step 4 of page 2.)
- 6.6.2024: **every time app.js changes, need to do this:**
    - `docker build . -t nodeapp`
    - then did `docker-compose up`
    - viewed and tested endpoints on port 3030
- 6.7.2024: doing CarMake and CarModel Django work
    - page 4, step 3, "Open djangoapp/views.py, import CarMake and..."
- 6.9.2024: finished
    - Started module 3, "Create Django Proxy Services of Backend APIs"
    - on step 5, start code engine
    - now on step 7, "Create Django views to get Dealers."
    - finished module 3.
    - TODO: begin module 4, Dynamic pages
- 6.10.2024
    - finished mod 4, step 3
    - TODO step 4
- 6.11.2024
    - did everything in step 4, but something's not working with the async stuff in the component.
    - I get an HTTP 200 after a second from the sentiment analyzer, but it doesn't ever load in the frontend.
- 6.12.2024
    - bugfix: changed djangoapp/urls.py, `get_dealer/<int:dealer_id>` to `dealer/<int:dealer_id>`.  didn't fix yet
    - bugfix: changed djangoapp/urls.py, `reviews/dealer/<int>` name to `dealer_details` from `dealer_reviews`.
    - bugfix: small mods to djangoapp/views.py/get_dealer_reviews.
    - finished step 4, dealer_id_reviews