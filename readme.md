<h1>Voting Booth</h1>
Last Updated: 9/01/21
<h2>Introduction</h2>
Voting Booth is meant to be a mobile application that allows USG to survey the student population. 
The project makes use of Django which is a Python based web framework.
<h2>Setup</h2>
<ol>
    <li>Download or Open PyCharm by JetBrains</li>
    <li>Select new project from Git or click the Git dropdown and select clone</li>
    <li>On the Voting Booth github page select the green code button and copy the link</li>
    <li>Paste the link in the URL section on PyCharm</li>
    <li>Once everything is finished go to File->Settings->Project:ask-meagain->Python Interpreter</li>
    <li>Add the following packages/libraries to the project:
        <ul>
            <li>Cython</li>
            <li>Django <-- download first</li>
            <li>PyJWT</li>
            <li>asgiref</li>
            <li>certifi</li>
            <li>cffi</li>
            <li>chardet</li>
            <li>charset-normalizer</li>
            <li>cryptography</li>
            <li>defusedxml</li>
            <li>django-social-auth</li>
            <li>httplib2</li>
            <li>idna</li>
            <li>oauth2</li>
            <li>oauthlib</li>
            <li>pip</li>
            <li>pycparser</li>
            <li>pyparsing</li>
            <li>python-openid</li>
            <li>python3-openid</li>
            <li>pytz</li>
            <li>pyusb</li>
            <li>requests</li>
            <li>requests-oauthlib</li>
            <li>setuptools</li>
            <li>six</li>
            <li>social-auth-app-django <-- download second</li>
            <li>social-auth-core</li>
            <li>sqlparse</li>
            <li>urlib3</li>
        </ul>
    </li>
    <li>Switch to the develop branch in the bottom right corner of PyCharm (if applicable)</li>
    <li>In the terminal window type "python manage.py runserver 8000"</li>
    <li>Click the link that appears in the terminal window</li>
</ol>
<h2>Other Notes</h2>
<ul>
    <li>https://www.djangoproject.com/ is your best start place for learning how to do something in Django</li>
    <li>Running makemigrations (see database_doc.md) should be tried early on when troubleshooting an unexpected issue</li>
</ul>
