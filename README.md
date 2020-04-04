   * [<span>Create folder DO_NOT_DELETE_djang_basic_documentation_part2</span>](#create-folder-do_not_delete_djang_basic_documentation_part2)
   * [<span>Create a new repoitory in github</span>](#create-a-new-repoitory-in-github)
      * [<span>[code] Initialize the git repository and set the remote urls</span>](#code-initialize-the-git-repository-and-set-the-remote-urls)
   * [<span>.gitignore Commit: Create the first commit for only gitignore</span>](#gitignore-commit-create-the-first-commit-for-only-gitignore)
   * [<span>Documentation Commit: Commit which will store the Documentation and .gitignore files</span>](#documentation-commit-commit-which-will-store-the-documentation-and-gitignore-files)
   * [<span></span>](#-1)
   * [<span>Base Commit 1: This is basically the basic_django folder from thirteenth Commit from django_basic_documentation</span>](#base-commit-1-this-is-basically-the-basic_django-folder-from-thirteenth-commit-from-django_basic_documentation)
   * [<span>Base Commit 2: Copy Pipfile and Pipfile.lock</span>](#base-commit-2-copy-pipfile-and-pipfilelock)
      * [<span>[code] Copy pipenv and piplock files and add them to the git</span>](#code-copy-pipenv-and-piplock-files-and-add-them-to-the-git)
   * [<span>Base Commit 3: Setup Virtual env: run pipenv install --dev (empty commit)</span>](#base-commit-3-setup-virtual-env-run-pipenv-install---dev-empty-commit)
      * [<span>[code] install the python virualenv (install dev packages also for development) </span>](#code-install-the-python-virualenv-install-dev-packages-also-for-development-)
      * [<span>[image] terminator screenshots of the above commands</span>](#image-terminator-screenshots-of-the-above-commands)
      * [<span>[code] Git commit</span>](#code-git-commit)
   * [<span>Base Commit 4: Create another database and copy into it</span>](#base-commit-4-create-another-database-and-copy-into-it)
      * [<span>[code] To copy a database in postgresql we do</span>](#code-to-copy-a-database-in-postgresql-we-do)
      * [<span>[code] To copy the database (actual)</span>](#code-to-copy-the-database-actual)
      * [<span>[image] How to copy a database</span>](#image-how-to-copy-a-database)
      * [<span>[code] Git commit</span>](#code-git-commit-1)
   * [<span>Base Commit </span><span>5</span><span>: </span><span>Copy .env file and change database name</span>](#base-commit-5-copy-env-file-and-change-database-name)
      * [<span>[code] We keep the .env file outside the project directory and link it form there. So we will create a folder where we will store the env file</span>](#code-we-keep-the-env-file-outside-the-project-directory-and-link-it-form-there-so-we-will-create-a-folder-where-we-will-store-the-env-file)
      * [<span>[code] We have to copy the .env file from the basic_django project and change the database name from basicdjangodb to basicdjangodb2 and then link .env file into the folder where wsgi.py resides</span>](#code-we-have-to-copy-the-env-file-from-the-basic_django-project-and-change-the-database-name-from-basicdjangodb-to-basicdjangodb2-and-then-link-env-file-into-the-folder-where-wsgipy-resides)
      * [<span>[code] Git commit</span>](#code-git-commit-2)
   * [<span>Basic Commit 6: Checking the server: runserver, redis and celery</span>](#basic-commit-6-checking-the-server-runserver-redis-and-celery)
      * [<span>Start redis server</span>](#start-redis-server)
         * [<span>[code] Start redis server</span>](#code-start-redis-server)
         * [<span>[image] start redis server</span>](#image-start-redis-server)
      * [<span>Start celery</span>](#start-celery)
         * [<span>[code] starting celery</span>](#code-starting-celery)
         * [<span>[image] staring celery</span>](#image-staring-celery)
      * [<span>Start runserver</span>](#start-runserver)
         * [<span>[code] start runserver</span>](#code-start-runserver)
         * [<span>[image] start runserver</span>](#image-start-runserver)
      * [<span>[code] Git commit</span>](#code-git-commit-3)
   * [<span>First Commit: Add TESTING_EMAIL2 to settings.py</span>](#first-commit-add-testing_email2-to-settingspy)
      * [<span>[code] edit settings.py and add testing_email2</span>](#code-edit-settingspy-and-add-testing_email2)
      * [<span>[image] add testing_email2 to settings.py</span>](#image-add-testing_email2-to-settingspy)
      * [<span>[image] commands to get the diff file and change   to     and - to ---</span>](#image-commands-to-get-the-diff-file-and-change--to--and---to----)
      * [<span>[image] settings.py diff file</span>](#image-settingspy-diff-file)
      * [<span>[code] create a commit</span>](#code-create-a-commit)
   * [<span></span>](#-2)
   * [<span>Second Commit: Add Django remote forms package</span>](#second-commit-add-django-remote-forms-package)
      * [<span>[code] how to get django_remote_forms and commit the changes</span>](#code-how-to-get-django_remote_forms-and-commit-the-changes)
      * [<span>[image] screenshot of terminator for this commit</span>](#image-screenshot-of-terminator-for-this-commit)
      * [<span>[code] Some sample Example</span>](#code-some-sample-example)
   * [<span>Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail</span>](#second-commit-example-using-django-remote-forms-an-api-endpoint-serving-remote-forms-of-userloginviaotpformemail)
      * [<span>[code] UserLoginViaOtpFormEmail (this already defined)</span>](#code-userloginviaotpformemail-this-already-defined)
      * [<span>[image]</span>](#image)
      * [<span>[code] api endpoint: api_user_login_via_otp_form_email_django_forms_example</span>](#code-api-endpoint-api_user_login_via_otp_form_email_django_forms_example)
      * [<span>[image]</span>](#image-1)
      * [<span>[code] urls.py</span>](#code-urlspy)
      * [<span>[image] urls.py </span>](#image-urlspy-)
      * [<span>[image] output after opening the link </span>](#image-output-after-opening-the-link-)
   * [<span>Third Commit: Add  node_module to gitignore</span>](#third-commit-add-node_module-to-gitignore)
      * [<span>[images] changing .gitignore</span>](#images-changing-gitignore)
   * [<span>Fourth Commit: Setup Nodejs project. Install webpack, webpack-bundle-tracker, react, react-dom, @babel/core babel-loader @babel/preset-env @babel/preset-react and django-webpack-loader (python)</span>](#fourth-commit-setup-nodejs-project-install-webpack-webpack-bundle-tracker-react-react-dom-babelcore-babel-loader-babelpreset-env-babelpreset-react-and-django-webpack-loader-python)
      * [<span>Webpack</span>](#webpack)
      * [<span>[code] npm init</span>](#code-npm-init)
      * [<span>[image] npm init</span>](#image-npm-init)
      * [<span>[code] Npm: Install webpack and webpack-bundle-tracker</span>](#code-npm-install-webpack-and-webpack-bundle-tracker)
      * [<span>[code] npm : Install reactjs and babel</span>](#code-npm--install-reactjs-and-babel)
      * [<span>[image] npm: package.json</span>](#image-npm-packagejson)
      * [<span>[code] .Babelrc for reactjs and  babel-loader to webpack.config.js [this is done in next commit. But shown here also]</span>](#code-babelrc-for-reactjs-and-babel-loader-to-webpackconfigjs-this-is-done-in-next-commit-but-shown-here-also)
      * [<span>[code] pipenv: install django-webpack-loader</span>](#code-pipenv-install-django-webpack-loader)
      * [<span>[code] Create empty webpack.config.js and .babelrc files</span>](#code-create-empty-webpackconfigjs-and-babelrc-files)
      * [<span>[images] npm init and install webpack, react, babel and django-webpack</span>](#images-npm-init-and-install-webpack-react-babel-and-django-webpack)
   * [<span>FIFTH COMMIT: Setup webpack.config.js, babelrc and settings.py </span>](#fifth-commit-setup-webpackconfigjs-babelrc-and-settingspy-)
      * [<span>[code] Add webpack_loader to INSTALLED_APPS</span>](#code-add-webpack_loader-to-installed_apps)
      * [<span>[code] configuring django-webpack-loader in settings.py</span>](#code-configuring-django-webpack-loader-in-settingspy)
      * [<span>[images] diff file</span>](#images-diff-file)
      * [<span>[code] webpack.config.js</span>](#code-webpackconfigjs)
      * [<span>[image] webpack config</span>](#image-webpack-config)
      * [<span>[code] .Babelrc for reactjs and  babel-loader(already added above but just shown) to webpack.config.js </span>](#code-babelrc-for-reactjs-and-babel-loaderalready-added-above-but-just-shown-to-webpackconfigjs-)
      * [<span>[image] .babelrc</span>](#image-babelrc)
      * [<span>[code] git staging and commiting the changes</span>](#code-git-staging-and-commiting-the-changes)
   * [<span>Sixth Commit: Compiling bundles using webpack and watch mode</span>](#sixth-commit-compiling-bundles-using-webpack-and-watch-mode)
      * [<span>[code] Compiling our bundle using webpack.config.js</span>](#code-compiling-our-bundle-using-webpackconfigjs)
      * [<span>[code] Watch mode for webpack.config.js:</span>](#code-watch-mode-for-webpackconfigjs)
   * [<span>Seventh Commit - A: Example of webpack and Reactjs:: Getting polls app</span>](#seventh-commit---a-example-of-webpack-and-reactjs-getting-polls-app)
      * [<span>[code] Go to the project folder (where .manage.py resides)</span>](#code-go-to-the-project-folder-where-managepy-resides)
      * [<span>[code] get the polls folder from github</span>](#code-get-the-polls-folder-from-github)
      * [<span>[code] Commit the changes</span>](#code-commit-the-changes)
   * [<span>Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app</span>](#seventh-commit-b-example-of-webpack-and-reactjs-setting-the-polls-app)
      * [<span>[code] Add polls_example_for_webpack_and_reactjs.polls to the installed INSTALLED_APPS</span>](#code-add-polls_example_for_webpack_and_reactjspolls-to-the-installed-installed_apps)
      * [<span>[code] Then make the migrations</span>](#code-then-make-the-migrations)
      * [<span>[code] Providing initial data for polls models</span>](#code-providing-initial-data-for-polls-models)
      * [<span>[code] Then add to the webpack.config.js the paths of the ReactJs files</span>](#code-then-add-to-the-webpackconfigjs-the-paths-of-the-reactjs-files)
      * [<span>[images] webpack.config.js</span>](#images-webpackconfigjs)
      * [<span>[code] Generate the bundle js using webpack and runserver and check whether the reactjs is working</span>](#code-generate-the-bundle-js-using-webpack-and-runserver-and-check-whether-the-reactjs-is-working)
      * [<span>[image] generate bundle and runserver and check urls</span>](#image-generate-bundle-and-runserver-and-check-urls)
      * [<span>[code] Then add to the urls of of the project</span>](#code-then-add-to-the-urls-of-of-the-project)
      * [<span>[code] After starting the server open the links:</span>](#code-after-starting-the-server-open-the-links)
      * [<span>[code] commit changes</span>](#code-commit-changes)
      * [<span>[image]</span>](#image-2)
   * [<span>EIGHT COMMIT: JWT TOKEN AUTHENTICATION</span>](#eight-commit-jwt-token-authentication)
      * [<span>[code-install] Install django-rest-framework</span>](#code-install-install-django-rest-framework)
      * [<span>[images] jwt procedure and functions</span>](#images-jwt-procedure-and-functions)
   * [<span>EIGHT B : Creating views to login using OTP with token method:</span>](#eight-b--creating-views-to-login-using-otp-with-token-method)
      * [<span>[code - install] postman</span>](#code---install-postman)
      * [<span>[code - commands ] Mkdir api inside login_register_password</span>](#code---commands--mkdir-api-inside-login_register_password)
      * [<span>[code - install]  </span><span>Django request logging</span>](#code---install-django-request-logging)
      * [<span>[code] downgrade redis to redis==3.3.11 for TypeError: unhashable type: 'Redis'</span>](#code-downgrade-redis-to-redis3311-for-typeerror-unhashable-type-redis)
      * [<span>[theory] </span><span>JWT’s Structure:</span>](#theory-jwts-structure)
      * [<span>[code - example] </span><span>Creating JSON Web token in python :-</span>](#code---example-creating-json-web-token-in-python--)
      * [<span>Create user_login_via_otp_form_email() method in views.py</span>](#create-user_login_via_otp_form_email-method-in-viewspy)
         * [<span>[code]Basic basic_django/login_register_password/api/views.py/user_login_via_otp_form_email()</span>](#codebasic-basic_djangologin_register_passwordapiviewspyuser_login_via_otp_form_email)
      * [<span>[code] Add to basic_django/login_register_password/api/urls.py</span>](#code-add-to-basic_djangologin_register_passwordapiurlspy)
         * [<span>Also add the api urls to the basic_django/login_register_password/urls.py</span>](#also-add-the-api-urls-to-the-basic_djangologin_register_passwordurlspy)
      * [<span>[code   image] curl - Test the api url</span>](#code--image-curl---test-the-api-url)
      * [<span>[Code] Create OTP using pyOTP</span>](#code-create-otp-using-pyotp)
         * [<span>Add to settings.py</span>](#add-to-settingspy)
         * [<span>[code settings.py]</span>](#code-settingspy)
         * [<span>[image settings.py]</span>](#image-settingspy)
         * [<span>[image - generate OTP and corresponding nonce]</span>](#image---generate-otp-and-corresponding-nonce)
         * [<span>[code  - generate OTP and corresponding nonce]</span>](#code---generate-otp-and-corresponding-nonce)
      * [<span>Philosophy behind the OTP creation and verification:</span>](#philosophy-behind-the-otp-creation-and-verification)
      * [<span>[code] user_login_via_otp_form_email </span>](#code-user_login_via_otp_form_email-)
         * [<span>[image] Basic structure</span>](#image-basic-structure)
      * [<span>Philosophy behind the api creation w.r.t messages and redirect:</span>](#philosophy-behind-the-api-creation-wrt-messages-and-redirect)
      * [<span>4xx vs 5xx http codes in rest api</span>](#4xx-vs-5xx-http-codes-in-rest-api)
      * [<span>Passing OTP and getting user token</span>](#passing-otp-and-getting-user-token)
      * [<span>[code] otp verification logic</span>](#code-otp-verification-logic)
      * [<span>[image] otp verification logic</span>](#image-otp-verification-logic)
      * [<span>Code for the user_login_via_otp_form_otp view:</span>](#code-for-the-user_login_via_otp_form_otp-view)
      * [<span>[code -- user_login_via_otp_form_otp]</span>](#code----user_login_via_otp_form_otp)
      * [<span>[image] FULL views.py file</span>](#image-full-viewspy-file)
      * [<span>[code] full views.py</span>](#code-full-viewspy)
      * [<span>[code] urls.py</span>](#code-urlspy)
      * [<span>[image] urls.py</span>](#image-urlspy)
      * [<span>[image] curl commands: Checking the urls using curl:</span>](#image-curl-commands-checking-the-urls-using-curl)
      * [<span>[code] curl commands:</span>](#code-curl-commands)
      * [<span>How to set logging time to IST</span>](#how-to-set-logging-time-to-ist)
      * [<span>Adding absolute path and Method in verbose in logging in settings.py</span>](#adding-absolute-path-and-method-in-verbose-in-logging-in-settingspy)
   * [<span>Miscellaneous</span>](#miscellaneous)
      * [<span>Webpack Main Concepts</span>](#webpack-main-concepts)
         * [<span>Entry</span>](#entry)
         * [<span>Output</span>](#output)
         * [<span>Loaders</span>](#loaders)
         * [<span>Plugins</span>](#plugins)
         * [<span>Mode</span>](#mode)
      * [<span>Webpack: how to have multiple entries and outputs and easily use them in template</span>](#webpack-how-to-have-multiple-entries-and-outputs-and-easily-use-them-in-template)
         * [<span>[code] settings.py</span>](#code-settingspy)
         * [<span>[code] Webpack.config.js:</span>](#code-webpackconfigjs)
         * [<span>[image] webpack.config.js</span>](#image-webpackconfigjs)
         * [<span>[code] templates/polls/index.html</span>](#code-templatespollsindexhtml)
         * [<span>[code] polls/urls.py</span>](#code-pollsurlspy)
         * [<span>[code] polls/views,py</span>](#code-pollsviewspy)
         * [<span>[code] polls/static/polls/js/index.js</span>](#code-pollsstaticpollsjsindexjs)
      * [<span>How to integrate Django API project with nodejs and react on frontend?. Why not to use SPA</span>](#how-to-integrate-django-api-project-with-nodejs-and-react-on-frontend-why-not-to-use-spa)
      * [<span>Webpack: Multiple entry points:</span>](#webpack-multiple-entry-points)
      * [<span>Webpack: path as the entry name: How to set multiple file entry and output in project with webpack?</span>](#webpack-path-as-the-entry-name-how-to-set-multiple-file-entry-and-output-in-project-with-webpack)
      * [<span>Webpack: multiple output paths</span>](#webpack-multiple-output-paths)
      * [<span>Django-webpack-loader: </span><span><a href="https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&amp;sa=D&amp;ust=1585972459483000" rel="nofollow">https://github.com/owais/django-webpack-loader</a></span>](#django-webpack-loader-httpsgithubcomowaisdjango-webpack-loader)
         * [<span>setup npm in the root of your django project:</span>](#setup-npm-in-the-root-of-your-django-project)
         * [<span>Npm dependencies</span>](#npm-dependencies)
         * [<span>Installing npm packages:</span>](#installing-npm-packages)
            * [<span>Note for babel:</span>](#note-for-babel)
         * [<span>save vs save-dev</span>](#save-vs-save-dev)
         * [<span>Create webpack config</span>](#create-webpack-config)
         * [<span>Create webpack config</span>](#create-webpack-config-1)
         * [<span>Directory Structure:</span>](#directory-structure)
         * [<span>Compiling our first bundle</span>](#compiling-our-first-bundle)
         * [<span>Watch mode:</span>](#watch-mode)
   * [<span>How to Take Screen shot of terminator:</span>](#how-to-take-screen-shot-of-terminator)
      * [<span>First we have to manually resize the terminator so that its cursor and the edge matche</span>](#first-we-have-to-manually-resize-the-terminator-so-that-its-cursor-and-the-edge-matche)
         * [<span>[image] wrong way to resize the terminator</span>](#image-wrong-way-to-resize-the-terminator)
         * [<span>[code] correct way to resize the terminator</span>](#code-correct-way-to-resize-the-terminator)
      * [<span>Create a file called terminator_screenshot.sh and copy the script into it</span>](#create-a-file-called-terminator_screenshotsh-and-copy-the-script-into-it)
         * [<span>[code] terminator screen shot script</span>](#code-terminator-screen-shot-script)
         * [<span>[image] terminator screenshot script</span>](#image-terminator-screenshot-script)
      * [<span>Create a keyboard shortcut for this script in KDE desktop env</span>](#create-a-keyboard-shortcut-for-this-script-in-kde-desktop-env)
      * [<span>Start taking screenshots</span>](#start-taking-screenshots)
      * [<span>Combine the screenshots</span>](#combine-the-screenshots)
         * [<span>[code] To combine all the images into one use the following command:</span>](#code-to-combine-all-the-images-into-one-use-the-following-command)
         * [<span>[image] to combine all the images into one</span>](#image-to-combine-all-the-images-into-one)
      * [<span>Break images into multiple images for the purpose of using them in google docs</span>](#break-images-into-multiple-images-for-the-purpose-of-using-them-in-google-docs)
         * [<span>[code] splitting the images vertically with aspect ratio of 900:600</span>](#code-splitting-the-images-vertically-with-aspect-ratio-of-900600)
         * [<span>[image] splitting images vertically</span>](#image-splitting-images-vertically)
      * [<span>Paste them into the google docs:</span>](#paste-them-into-the-google-docs)
      * [<span>Using gimp to split images using guides and keep required images and then combine them.</span>](#using-gimp-to-split-images-using-guides-and-keep-required-images-and-then-combine-them)
      * [<span>Django putting all the apps in subfolder:</span>](#django-putting-all-the-apps-in-subfolder)
         * [<span>Question:</span>](#question)
         * [<span>Answer:</span>](#answer)
      * [<span>Using fixtures when apps are in subdirectories:</span>](#using-fixtures-when-apps-are-in-subdirectories)
         * [<span>[images] </span><span><a href="https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&amp;sa=D&amp;ust=1585972459551000" rel="nofollow">https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error</a></span>](#images-httpsstackoverflowcomquestions10313475moving-django-apps-into-subfolder-and-url-py-error)
         * [<span>[images] how to tackle with testing error when using subfolders <a href="https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder" rel="nofollow">https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder</a></span>](#images-how-to-tackle-with-testing-error-when-using-subfolders-httpsstackoverflowcomquestions6483636how-to-test-django-application-placed-in-subfolder)
      * [<span>To list the untracked files in the stash:</span>](#to-list-the-untracked-files-in-the-stash)
      * [<span>“Git stash apply” all files, except one</span>](#git-stash-apply-all-files-except-one)
      * [<span>Tree: how to exclude certain folderr and paths</span>](#tree-how-to-exclude-certain-folderr-and-paths)
         * [<span>[code]</span>](#code)
         * [<span>[images] we want to avoid files from templates/fixtures/migrations not to be shown</span>](#images-we-want-to-avoid-files-from-templatesfixturesmigrations-not-to-be-shown)
      * [<span>JWT TOKEN:</span>](#jwt-token)
         * [<span>JWT’s Structure:</span>](#jwts-structure)
         * [<span>Creating JSON Web token in python :-</span>](#creating-json-web-token-in-python--)
      * [<span>Headers vs Params</span>](#headers-vs-params)
      * [<span>What's the difference between the square bracket and dot notations in Python?</span>](#whats-the-difference-between-the-square-bracket-and-dot-notations-in-python)
      * [<span>POSTMAN content-type</span>](#postman-content-type)
      * [<span>Django HTTP headers stores with a prefix HTTP_</span>](#django-http-headers-stores-with-a-prefix-http_)
         * [<span>[images] HTTP_ prefix</span>](#images-http_-prefix)
      * [<span>Bytes vs String Python</span>](#bytes-vs-string-python)
         * [<span>[images]</span>](#images)
      * [<span>Python Split() : </span>](#python-split--)
         * [<span>[images]</span>](#images-1)
      * [<span>Logic of get_jwt_value of django-rest-framework-jwt:</span>](#logic-of-get_jwt_value-of-django-rest-framework-jwt)
         * [<span>[images]</span>](#images-2)
      * [<span>How to use django 3.0 ORM in a Jupyter Notebook without triggering the async context check?</span>](#how-to-use-django-30-orm-in-a-jupyter-notebook-without-triggering-the-async-context-check)
      * [<span>Django request logging:</span>](#django-request-logging)
      * [<span>If you can decode JWT how are they secure?</span>](#if-you-can-decode-jwt-how-are-they-secure)
      * [<span>Encrypt and decrypt in Django - Ans: better is database</span>](#encrypt-and-decrypt-in-django---ans-better-is-database)
      * [<span>How to do hashing more securely - streched hashing</span>](#how-to-do-hashing-more-securely---streched-hashing)
      * [<span>Hashing: always use different salt for hash:</span>](#hashing-always-use-different-salt-for-hash)
      * [<span>Attacker sniffs and knows all the api end points and makes better app</span>](#attacker-sniffs-and-knows-all-the-api-end-points-and-makes-better-app)
      * [<span>Hmac how it works and two main merits:</span>](#hmac-how-it-works-and-two-main-merits)
      * [<span>JWT why payload is not encrpted - Reason: the cost (however small it is) exceeds the benefit,</span>](#jwt-why-payload-is-not-encrpted---reason-the-cost-however-small-it-is-exceeds-the-benefit)
      * [<span>JSON web token - password in the payload?    DONT DO IT</span>](#json-web-token---password-in-the-payload--dont-do-it)
      * [<span>HMAC  is symmetric whereas assymetric takes more computing</span>](#hmac-is-symmetric-whereas-assymetric-takes-more-computing)
      * [<span>How does HOTP keep in sync?</span>](#how-does-hotp-keep-in-sync)
      * [<span>Bits and Bytes and characters and how computer stores</span>](#bits-and-bytes-and-characters-and-how-computer-stores)
      * [<span>How HEX is stored</span>](#how-hex-is-stored)
      * [<span>(Python) view bytes in binary</span>](#python-view-bytes-in-binary)
      * [<span>Code points to bytes using encoding</span>](#code-points-to-bytes-using-encoding)
      * [<span>What is unicode and what is UTF-8 etc</span>](#what-is-unicode-and-what-is-utf-8-etc)
      * [<span>(python) Bytes are encoded bytes not code poitns</span>](#python-bytes-are-encoded-bytes-not-code-poitns)
      * [<span>(python) ** While encoding using UTF-8 into bytes code points which are greater than FF are encoded (i.e mapped) as combination of multiple ascii extended codepoints</span>](#python--while-encoding-using-utf-8-into-bytes-code-points-which-are-greater-than-ff-are-encoded-ie-mapped-as-combination-of-multiple-ascii-extended-codepoints)
      * [<span>(python) Difference between chr() and bytes.decode</span>](#python-difference-between-chr-and-bytesdecode)
      * [<span>Urandom: os.urandom() generates operating-system-dependent random bytes that can safely be called cryptographically secure:</span>](#urandom-osurandom-generates-operating-system-dependent-random-bytes-that-can-safely-be-called-cryptographically-secure)
      * [<span>timetuple()</span>](#timetuple)
      * [<span>time.mktime() to convert to seconds from epoch</span>](#timemktime-to-convert-to-seconds-from-epoch)
      * [<span>HMAC implementation in python</span>](#hmac-implementation-in-python)
      * [<span>pyOTP - TOTP  How to change interval</span>](#pyotp---totp-how-to-change-interval)
      * [<span>Hash Function - Collision resistance</span>](#hash-function---collision-resistance)
      * [<span>What is the difference between a HMAC and a hash of data?</span>](#what-is-the-difference-between-a-hmac-and-a-hash-of-data)
      * [<span>Is it possible to reverse a sha1?</span>](#is-it-possible-to-reverse-a-sha1)
      * [<span>What is hashing</span>](#what-is-hashing)
      * [<span> How to hack a hash</span>](#how-to-hack-a-hash)
      * [<span>HMAC vs salted hash</span>](#hmac-vs-salted-hash)
      * [<span>HMAC vs salted hash for password</span>](#hmac-vs-salted-hash-for-password)
      * [<span>What is the difference between hash salting and noncing?</span>](#what-is-the-difference-between-hash-salting-and-noncing)
      * [<span>(Python) for loop in range</span>](#python-for-loop-in-range)
      * [<span>(python) Get random string in python:</span>](#python-get-random-string-in-python)
      * [<span>Django: How will django protect from knowing the passwords by using hashes if someone have access to the database</span>](#django-how-will-django-protect-from-knowing-the-passwords-by-using-hashes-if-someone-have-access-to-the-database)
      * [<span>Difference between Hashing a Password and Encrypting it</span>](#difference-between-hashing-a-password-and-encrypting-it)
      * [<span>Difference between salted hash and keyed hashing?</span>](#difference-between-salted-hash-and-keyed-hashing)
      * [<span>What key is used for hmac in PBKDF2</span>](#what-key-is-used-for-hmac-in-pbkdf2)
      * [<span>Reply ATTACK - Solution using  Nonce to keep a message unique from all other messages</span>](#reply-attack---solution-using-nonce-to-keep-a-message-unique-from-all-other-messages)
      * [<span>TOTP Base32 vs Base64</span>](#totp-base32-vs-base64)
      * [<span><a href="https://www.google.com/url?q=https://cryptii.com/pipes/hex-to-base32&amp;sa=D&amp;ust=1585972459621000" rel="nofollow">https://cryptii.com/pipes/hex-to-base32</a></span>](#httpscryptiicompipeshex-to-base32)
      * [<span>Hexadecimal</span>](#hexadecimal)
      * [<span>Convert binary to Hex</span>](#convert-binary-to-hex)
      * [<span>(python) How to create secret key i.e base32-formatted</span>](#python-how-to-create-secret-key-ie-base32-formatted)
      * [<span>(python - nonce) What is the standard method for generating a nonce in Python?</span>](#python---nonce-what-is-the-standard-method-for-generating-a-nonce-in-python)
      * [<span>(python - secret token) </span><span>The New Way To Generate Secure Tokens in Python</span>](#python---secret-token-the-new-way-to-generate-secure-tokens-in-python)
      * [<span>(python - secure random) </span><span>Cryptographically Secure Random Data in Python</span>](#python---secure-random-cryptographically-secure-random-data-in-python)
      * [<span>(python - nonce) Another way to generate nonce in python</span>](#python---nonce-another-way-to-generate-nonce-in-python)
      * [<span>What is the difference between a digest and a hash function?</span>](#what-is-the-difference-between-a-digest-and-a-hash-function)
      * [<span>What is hash</span>](#what-is-hash)
      * [<span> Base64 encoding vs Base64url encoding </span>](#base64-encoding-vs-base64url-encoding-)
      * [<span>Difference between ASCII and UNICODE ?</span>](#difference-between-ascii-and-unicode-)
      * [<span>Ascii 7-bit</span>](#ascii-7-bit)
      * [<span>ASCII table</span>](#ascii-table)
      * [<span>ASCII Converter - Hex, decimal, binary, base64, and ASCII converter</span>](#ascii-converter---hex-decimal-binary-base64-and-ascii-converter)
      * [<span>How Text strings are stored in computer</span>](#how-text-strings-are-stored-in-computer)
      * [<span>(Python) how strings are stored</span>](#python-how-strings-are-stored)
      * [<span>(Python) convert a integer to unicode character</span>](#python-convert-a-integer-to-unicode-character)
      * [<span>(python/unicode) U  u’  (unicode code points representation)</span>](#pythonunicode-u-u-u2-unicode-code-points-representation)
      * [<span>Unicode Code point:</span>](#unicode-code-point)
      * [<span>(Python) byte literal (b preix) and plain string </span>](#python-byte-literal-b-preix-and-plain-string-)
      * [<span>(python) Bytes object</span>](#python-bytes-object)
         * [<span>Explaining the rules for bytes object and ascii characters</span>](#explaining-the-rules-for-bytes-object-and-ascii-characters)
      * [<span>Encode to str to byte and decode byte to str</span>](#encode-to-str-to-byte-and-decode-byte-to-str)
      * [<span>Unicode is not encoding:</span>](#unicode-is-not-encoding)
      * [<span>Code Point</span>](#code-point)
      * [<span>UTF 32 vs UTF-16 vs UTF - 8</span>](#utf-32-vs-utf-16-vs-utf---8)
      * [<span>(Python) </span><span>Testing unicode, byte and encoding:</span>](#python-testing-unicode-byte-and-encoding)
      * [<span>Symmetric vs asymetric keys</span>](#symmetric-vs-asymetric-keys)
      * [<span>(python) </span><span>Django Random secret i.e secrets.choice vs secrets.token_urlsafe</span>](#python-django-random-secret-ie-secretschoice-vs-secretstoken_urlsafe)
      * [<span>(python) Saving utf-8 texts in json.dumps as UTF8, not as \u escape sequence</span>](#python-saving-utf-8-texts-in-jsondumps-as-utf8-not-as-u-escape-sequence)
      * [<span>(Python) String literals truncated \UXXXXXXXX escape</span>](#python-string-literals-truncated-uxxxxxxxx-escape)
      * [<span>(jupyter) Adding word wrap to jupyter</span>](#jupyter-adding-word-wrap-to-jupyter)
      * [<span>(jupyter) Bringing the scrol bar to main page in jupyter</span>](#jupyter-bringing-the-scrol-bar-to-main-page-in-jupyter)
         * [<span>Problem:</span>](#problem)
      * [<span>(Python) raw text and escapes</span>](#python-raw-text-and-escapes)
      * [<span>Website Unicode Code Character, character, utf-8, Decomposition, Lowercase Character:</span>](#website-unicode-code-character-character-utf-8-decomposition-lowercase-character)
      * [<span>Unicode character dotted circle used for displaying diacratics etc while combination characters</span>](#unicode-character-dotted-circle-used-for-displaying-diacratics-etc-while-combination-characters)
      * [<span>(Python) Unicode combination characters example</span>](#python-unicode-combination-characters-example)
      * [<span>unicode: find out the corresponding single unicode for a character formed by combination of unicodes [duplicate]: (Normalizing Unicode)</span>](#unicode-find-out-the-corresponding-single-unicode-for-a-character-formed-by-combination-of-unicodes-duplicate-normalizing-unicode)
      * [<span>Unicode characters Non combined to Combined and back</span>](#unicode-characters-non-combined-to-combined-and-back)
      * [<span>Byte to Bytearray and reverse</span>](#byte-to-bytearray-and-reverse)
      * [<span>Firefox remove headers</span>](#firefox-remove-headers)
      * [<span>(python) PyOTP secret cannot be a non base32 type</span>](#python-pyotp-secret-cannot-be-a-non-base32-type)
      * [<span>How to convert a string to base32 string and back</span>](#how-to-convert-a-string-to-base32-string-and-back)
      * [<span>Python replace</span>](#python-replace)
      * [<span>Sublime text navigating python code</span>](#sublime-text-navigating-python-code)
      * [<span>How to present the code for documentation:</span>](#how-to-present-the-code-for-documentation)
* # Create folder DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ cd /home/web_dev<br>$ mkdir DO_NOT_DELETE_djang_basic_documentation_part2<br></td></tr></tbody></table>

* # Create a new repoitory in github

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Go to<br><a href="https://www.google.com/url?q=https://github.com/new&amp;sa=D&amp;ust=1585972458517000" class="c14">https://github.com/new</a><br><br>Then add a name: django_basic_documentation_ver2<br><br>Dont select README<br><br>The new url of the github project is<br><br><a href="https://www.google.com/url?q=https://github.com/sant527/django_basic_documentation_ver2&amp;sa=D&amp;ust=1585972458518000" class="c14">https://github.com/sant527/django_basic_documentation_ver2</a><br></td></tr></tbody></table>

 * ## \[code\] Initialize the git repository and set the remote urls

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd /home/web+dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>## Initialize git<br> simha [&lt;&gt;] /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2 [&lt;&gt;]<br>$ git init<br>Initialized empty Git repository in /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.git/<br><br>## To see which remote servers you have configured. Currently none . It lists the shortnames of each remote handle you’ve specified<br> simha [&lt;&gt;] /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2 [&lt;&gt;]  master ✔ [&lt;&gt;]<br>$ git remote -v                                                                   <br><br>## add remote server (default shortname is origin)<br> ✘ [&lt;&gt;] simha [&lt;&gt;] /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2 [&lt;&gt;]  master ✔ [&lt;&gt;]<br>$ git remote add origin git@github.com:sant527/django_basic_documentation_ver2.git                                                                           <br><br>## again view remote server<br> simha [&lt;&gt;] /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2 [&lt;&gt;]  master ✔ [&lt;&gt;]<br>$ git remote -v                                                                   <br>origin        git@github.com:sant527/django_basic_documentation_ver2.git (fetch)<br>origin        git@github.com:sant527/django_basic_documentation_ver2.git (push)<br></td></tr></tbody></table>

* # .gitignore Commit: Create the first commit for only gitignore

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>### Out first commit will have all the documentation files and the gitignore files: We will put the documentation files later. But currently we will put the .gitignore<br><br>## Copy the .gitignore from the django_basic_documentation github.<br> 18:33:31  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔<br>$  svn ls https://github.com/sant527/django_basic_documentation<br>branches/<br>trunk/<br><br> 18:33:47  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔<br>$  svn ls https://github.com/sant527/django_basic_documentation/trunk<br>.gitignore<br>Other_Docs_and_Misc/<br>Pipfile<br>Pipfile.lock<br>README.md<br>basic_django/<br>images/<br><br> 18:34:01  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔<br>$ svn export -r13 https://github.com/sant527/django_basic_documentation/trunk/.gitignore  <br>A    .gitignore<br>Export complete.<br><br>## stage and commit<br>$ git add -A<br>$ git commit -m '.gitignore Commit: The .gitignore file for this project.'<br></td></tr></tbody></table>

* # Documentation Commit: Commit which will store the Documentation and .gitignore files

* # 

     * |                                                                                                            |

     * | ---------------------------------------------------------------------------------------------------------- |

     * | git commit --allow-empty -m 'Documentation Commit: Commit which will store the Documentation' |

* # 

* # Base Commit 1: This is basically the basic\_django folder from thirteenth Commit from django\_basic\_documentation

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The github url is:<br><a href="https://www.google.com/url?q=https://github.com/sant527/django_basic_documentation&amp;sa=D&amp;ust=1585972458528000" class="c14">https://github.com/sant527/django_basic_documentation</a><br><br>Now we want to get the basic_django from the last or 13th commit<br><br>We will use svn to export a particular folder from git<br><br>$ svn log https://github.com/sant527/django_basic_documentation<br>------------------------------------------------------------------------<br>r13 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Thirteenth Commit: This is example for Third Commit custom logging and pretty print functions<br><br>------------------------------------------------------------------------<br>r12 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Twelveth Commit: Logging via email and OTP, views,forms, templates<br><br>------------------------------------------------------------------------<br>r11 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Eleventh_A Commit: add articles and login_register_password apps to settings<br><br>------------------------------------------------------------------------<br>r10 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Eleventh Commit: create articles and login_register_password app<br><br>------------------------------------------------------------------------<br>r9 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Ninth Commit:  Added custom model and manager and AUTH_USER_MODEL to settings and migrate<br><br>------------------------------------------------------------------------<br>r8 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Sixth_A Commit: Add the app to the settings<br><br>------------------------------------------------------------------------<br>r7 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Sixth Commit: creating an app for custom_user using manage.py startapp<br><br>------------------------------------------------------------------------<br>r6 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>FIFTH COMMIT: Celery and redis<br><br>------------------------------------------------------------------------<br>r5 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>FOURTH COMMIT: creating new gmail account, use 2 step verification, create app password, DJANO email config, view to send email<br><br>------------------------------------------------------------------------<br>r4 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>THIRD COMMIT: pretty print obj, sql, pygment, sqlparse, django-extensions, ipython, jupyter, runserver_plus, werkzeug, graph_models, django-querycount, pudb debugger, logging - start,stop, custom format, filters, traceback<br><br>------------------------------------------------------------------------<br>r3 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Second Commit: django-environ and .env and setttings.py and psycopg2 and sensitive information secure<br><br>------------------------------------------------------------------------<br>r2 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>First Commit: Fresh virtualenv with pipenv and install django and remove SECRETKEY<br><br>------------------------------------------------------------------------<br>r1 | santhosh | 2019-10-18 12:02:36 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Zero Commit: Documentation Django, git, awk, commands, gitignore<br><br>------------------------------------------------------------------------<br><br>It show r1, r2, r3 etc and the corresponding commit<br><br>From above r13 is the latest revision<br><br>$ svn ls -r13 https://github.com/sant527/django_basic_documentation<br>branches/<br>trunk/<br><br>$ svn ls -r13 https://github.com/sant527/django_basic_documentation/trunk<br>.gitignore<br>DjangoDocumentation_docx_and_htmlzip/<br>Pipfile<br>Pipfile.lock<br>README.md<br>awkdoc/<br>basic_django/<br>commands.txt<br>flowcharts/<br>gitdoc/<br>images/<br><br>## get the basic_django folder<br>$ svn export -r13 https://github.com/sant527/django_basic_documentation/trunk/basic_django<br><br>The above command will export the folder to here<br><br>$ ls -al<br>total 24<br>drwxr-xr-x  4 simha users 4096 Nov 22 23:22 .<br>drwxr-xr-x 39 simha users 4096 Nov 21 18:53 ..<br>drwxr-xr-x  7 simha users 4096 Nov 22 23:22 basic_django<br>drwxr-xr-x  8 simha users 4096 Nov 22 23:24 .git<br>-rw-r--r--  1 simha users 4892 Nov 22 23:18 .gitignore<br><br>$ git status<br>On branch master<br>Untracked files:<br>  (use "git add &lt;file&gt;..." to include in what will be committed)<br><br>        basic_django/<br><br>nothing added to commit but untracked files present (use "git add" to track)<br><br>https://stackoverflow.com/questions/39030116/how-to-see-untracked-files-in-git-instead-of-untracked-directory?rq=1<br>NOTE: If git only shows that the directory is untracked, then every file in it (including files in subdirectories) is untracked.<br><br>If you have some ignored files in the directory, pass the -u flag when running git status (i.e., git status -u) to show the status of individual untracked files.<br><br>$ git status -u<br>On branch master<br>Untracked files:<br>  (use "git add &lt;file&gt;..." to include in what will be committed)<br><br>        basic_django/articles/__init__.py<br>        basic_django/articles/admin.py<br>        basic_django/articles/apps.py<br>        basic_django/articles/migrations/__init__.py<br>        basic_django/articles/models.py<br>        basic_django/articles/templates/articles/base.html<br>        basic_django/articles/templates/articles/main_page/articles.html<br>        basic_django/articles/tests.py<br>        basic_django/articles/urls.py<br>        basic_django/articles/views.py<br>        basic_django/basic_django/.env.example<br>        basic_django/basic_django/__init__.py<br>        basic_django/basic_django/celery.py<br>        basic_django/basic_django/settings.py<br>        basic_django/basic_django/tasks.py<br>        basic_django/basic_django/urls.py<br>        basic_django/basic_django/views.py<br>        basic_django/basic_django/wsgi.py<br>        basic_django/custom_user/__init__.py<br>        basic_django/custom_user/admin.py<br>        basic_django/custom_user/apps.py<br>        basic_django/custom_user/fixtures/ActionTypeForUserSessionLog.json<br>        basic_django/custom_user/migrations/0001_initial.py<br>        basic_django/custom_user/migrations/0002_auto_20191016_0203.py<br>        basic_django/custom_user/migrations/0003_auto_20191017_1002.py<br>        basic_django/custom_user/migrations/__init__.py<br>        basic_django/custom_user/models.py<br>        basic_django/custom_user/tests.py<br>        basic_django/custom_user/views.py<br>        basic_django/login_register_password/__init__.py<br>        basic_django/login_register_password/admin.py<br>        basic_django/login_register_password/apps.py<br>        basic_django/login_register_password/forms.py<br>        basic_django/login_register_password/migrations/__init__.py<br>        basic_django/login_register_password/models.py<br>        basic_django/login_register_password/templates/login_register_password/base.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/email/login_otp_sendemail.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/user_login_via_otp_form_email.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/user_login_via_otp_form_otp.html<br>        basic_django/login_register_password/tests.py<br>        basic_django/login_register_password/urls.py<br>        basic_django/login_register_password/views.py<br>        basic_django/manage.py<br>        basic_django/querycount_mod/__init__.py<br>        basic_django/querycount_mod/middleware.py<br>        basic_django/querycount_mod/middleware_backup.py<br>        basic_django/querycount_mod/qc_settings.py<br><br>nothing added to commit but untracked files present (use "git add" to track)<br><br>$ git add -A<br><br>$ git commit -m 'Base Commit: This is basically the basic_django folder from thirteenth Commit from django_basic_documentation'<br></td></tr></tbody></table>

* # Base Commit 2: Copy Pipfile and Pipfile.lock

 * ## \[code\] Copy pipenv and piplock files and add them to the git

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ svn export https://github.com/sant527/django_basic_documentation/trunk/Pipfile.lock<br><br>$ svn export https://github.com/sant527/django_basic_documentation/trunk/Pipfile<br><br>$ Git add -A<br><br>$ git commit -m 'Base Commit 2: Copy Pipfile and Pipfile.lock'<br></td></tr></tbody></table>

* # Base Commit 3: Setup Virtual env: run pipenv install --dev (empty commit)

 * ## \[code\] install the python virualenv (install dev packages also for development) 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$ export PIPENV_VENV_IN_PROJECT=1<br><br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$ pipenv shell<br>Creating a virtualenv for this project…<br>Pipfile: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/Pipfile<br>Using /usr/bin/python (3.7.3) to create virtualenv…<br>⠴ Creating virtual environment...Already using interpreter /usr/bin/python<br>Using base prefix '/usr'<br>New python executable in /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/python<br>Installing setuptools, pip, wheel...<br>done.<br><br>✔ Successfully created virtual environment! <br>Virtualenv location: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>## To install dev packages also use<br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔ <br>$ pipenv install --dev <br>Installing dependencies from Pipfile.lock (235b42)…<br>  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 65/65 — 00:00:36<br><br></td></tr></tbody></table>

 * ## \[image\] terminator screenshots of the above commands

     * ![](images/image102.png)

 * ## \[code\] Git commit

     * |                                                                                                                  |

     * | ---------------------------------------------------------------------------------------------------------------- |

     * | git commit --allow-empty -m 'Base Commit 3: Setup Virtual env: run pipenv install --dev' |

* # Base Commit 4: Create another database and copy into it

     * We have used  a database called basic “basicdjangodb” in the “django\_basic\_documentation” project

     * Since we are going to start off from there. We will work in a different database by copying it

 * ## \[code\] To copy a database in postgresql we do

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ psql -c “CREATE DATABASE newdb WITH TEMPLATE originaldb OWNER dbuser;”<br><br>Inour case:<br>Originaldb = basicdjangodb<br>Newdb = basicdjangodb2<br>Owner: we will keep the same owner for this database.<br>To know the owner of the We can list all the databases using <br>$ psql -c "\l"<br>And find the owner for basicdjangodb<br></td></tr></tbody></table>

 * ## \[code\] To copy the database (actual)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>&gt;&gt; 15:09:08 &gt;&gt; simha &gt;&gt; ~ &gt;&gt;<br>$ <br><br>#####   Change to root User<br>&gt;&gt; 15:09:09 &gt;&gt; simha &gt;&gt; ~ &gt;&gt;<br>$ su<br>Password: <br><br>#####   Change to postgres User<br>&gt;&gt; root@ &gt;&gt; /home/simha &gt;&gt;<br>#  su - postgres<br><br>#####   To view all the list of users<br>[postgres@gauranga ~]$ psql -c "\du"<br>                                    List of roles<br>  Role name  |                         Attributes                         | Member of <br>-------------+------------------------------------------------------------+-----------<br>………<br><br>#####   To view all the list of databases<br>[postgres@gauranga ~]$ psql -c "\l"<br>                                     List of databases<br>     Name      |    Owner    | Encoding |   Collate   |    Ctype    |   Access privileges   <br>---------------+-------------+----------+-------------+-------------+-----------------------<br>……...<br>(10 rows)<br><br>#####   To create a database copy of basicdjangodb with the user<br>[postgres@gauranga ~]$ psql -c "CREATE DATABASE basicdjangodb2 WITH TEMPLATE basicdjangodb OWNER basicdjango;"<br>CREATE DATABASE<br><br>#####   To view all the list of databases<br>[postgres@gauranga ~]$ psql -c "\l"<br>                                      List of databases<br>      Name      |    Owner    | Encoding |   Collate   |    Ctype    |   Access privileges   <br>----------------+-------------+----------+-------------+-------------+-----------------------<br>……...<br>(11 rows)<br><br>[postgres@gauranga ~]$ exit<br>logout<br><br>&gt;&gt; root@ &gt;&gt; /home/simha &gt;&gt;<br>#  exit<br><br>&gt;&gt; 15:17:04 &gt;&gt; simha &gt;&gt; ~ &gt;&gt;<br>$ <br></td></tr></tbody></table>

 * ## \[image\] How to copy a database

     * ![](images/image91.png)![](images/image275.png)![](images/image51.png)

 * ## \[code\] Git commit

     * |                                                                                                               |

     * | ------------------------------------------------------------------------------------------------------------- |

     * | git commit --allow-empty -m 'Base Commit 4: Create another database and copy into it' |

* # Base Commit 5: Copy .env file and change database name

 * ## \[code\] We keep the .env file outside the project directory and link it form there. So we will create a folder where we will store the env file

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd /home/web_dev/DONT_DELETE_env_django_basic_documentation<br><br>Mkdir DO_NOT_DELETE_djang_basic_documentation_part2<br><br>OR (with full path)<br><br>Mkdir /home/web_dev/DONT_DELETE_env_django_basic_documentation/DO_NOT_DELETE_djang_basic_documentation_part2<br></td></tr></tbody></table>

 * ## \[code\] We have to copy the .env file from the basic\_django project and change the database name from basicdjangodb to basicdjangodb2 and then link .env file into the folder where wsgi.py resides

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#guranga<br>cp /home/web_dev/DONT_DELETE_env_django_basic_documentation/django_basic_documentation/.env /home/web_dev/DONT_DELETE_env_django_basic_documentation/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>Edit .env file and change the database name from basicdjangodb to basicdjangodb2<br><br>DATABASE_URL=psql://user:pass@127.0.0.1:5432/basicdjangodb2<br><br>NOW LINK THE .env file into the project directory<br>ln -s /home/web_dev/DONT_DELETE_env_django_basic_documentation/DO_NOT_DELETE_djang_basic_documentation_part2/.env  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/basic_django/.env<br></td></tr></tbody></table>

 * ## \[code\] Git commit

     * |                                                                                                              |

     * | ------------------------------------------------------------------------------------------------------------ |

     * | git commit --allow-empty -m 'Base Commit 5: Copy .env file and change database name' |

* # Basic Commit 6: Checking the server: runserver, redis and celery

     * Before we start working, we want to check everything is working well from the previous example django\_basic

 * ## Start redis server

     * ### \[code\] Start redis server

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>### Change to root<br>$ su<br>Password:<br><br>### Start redis-server<br>$ redis-server<br></td></tr></tbody></table>

     * ### \[image\] start redis server

       * ![](images/image209.png)

 * ## Start celery

     * ### \[code\] starting celery

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> simha  ~<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$ pipenv shell<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✭<br>$ cd basic_django <br><br> simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✭<br>$ celery -A basic_django worker --loglevel=debug #ensure redis-server is running in root<br><br><br><br></td></tr></tbody></table>

     * ### \[image\] staring celery

       * ![](images/image4.png)

       * ![](images/image136.png)

 * ## Start runserver

     * ### \[code\] start runserver

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#### change directory<br> 17:41:03  simha  ~<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>#### start virtual env<br> 17:41:09  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$ pipenv shell<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> 17:41:12  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>#### change to project directory<br> 17:41:12  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✭<br>$ cd basic_django <br><br>#### start runserver<br> 17:41:17  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✭<br>$ ./manage.py runserver<br>Watching for file changes with StatReloader<br>Performing system checks...<br><br>System check identified no issues (0 silenced).<br>December 02, 2019 - 12:11:22<br>Django version 2.2.6, using settings 'basic_django.settings'<br>Starting development server at http://127.0.0.1:8000/<br>Quit the server with CONTROL-C.<br></td></tr></tbody></table>

     * ### \[image\] start runserver

       * ![](images/image69.png)

 * ## \[code\] Git commit

     * |                                                                                                                        |

     * | ---------------------------------------------------------------------------------------------------------------------- |

     * | git commit --allow-empty -m 'Basic Commit 6: Checking the server: runserver, redis and celery' |

* # First Commit: Add TESTING\_EMAIL2 to settings.py

     * We want to create TESTING\_EMAIL2="<test@xyz.com>" which will be used while showing any examples in github.

 * ## \[code\] edit settings.py and add testing\_email2

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Edit settings.py and add TESTING_EMAIL2<br><br># we want to use this mainly to show in github any example<br>TESTING_EMAIL2="test@xyz.com"<br></td></tr></tbody></table>

 * ## \[image\] add testing\_email2 to settings.py

     * ![](images/image156.png)

 * ## \[image\] commands to get the diff file and change + to +++ and - to ---

     * ![](images/image108.png)

 * ## \[image\] settings.py diff file

     * ![](images/image189.png)

 * ## \[code\] create a commit

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ Git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   basic_django/settings.py<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br>Git add -A<br><br> 19:34:54  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✚<br>$ git commit -m 'First Commit: Add TESTING_EMAIL2 to settings.py'                                     <br>[master fd300e2] First Commit: Add TESTING_EMAIL2 to settings.py<br> 1 file changed, 2 insertions(+)<br><br><br></td></tr></tbody></table>

* # 

* # Second Commit: Add Django remote forms package

     * [https://github.com/WiserTogether/django-remote-forms](https://www.google.com/url?q=https://github.com/WiserTogether/django-remote-forms&sa=D&ust=1585972458590000)

     * A package that allows you to serialize django forms, including fields and widgets into Python dictionary for easy conversion into JSON and expose over API

 * ## \[code\] how to get django\_remote\_forms and commit the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The github url is:<br><a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1585972458592000" class="c14">https://github.com/sant527/django_remote_forms</a><br><br>Now we want to get the django_remote_forms from the last or latest commit<br><br>We will use svn to export a particular folder from git<br><br>### change into the project folder<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django<br><br>### check the folder structure<br>$ tree -L 1 -a<br><br>### get the log of svn<br>$ svn log <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1585972458594000" class="c14">https://github.com/sant527/django_remote_forms</a><br><br>### check the folder <br>$ svn ls -r1 <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1585972458594000" class="c14">https://github.com/sant527/django_remote_forms</a><br>branches/<br>trunk/<br><br>### check the folder <br>$ svn ls -r1 <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms/trunk&amp;sa=D&amp;ust=1585972458595000" class="c14">https://github.com/sant527/django_remote_forms/trunk</a><br>django_remote_forms/<br><br>### export the folder here<br>$ svn export -r1 https://github.com/sant527/django_remote_forms/trunk/django_remote_forms<br><br>### check the folder structure<br>$ tree -L 1 -a<br><br>### check git status<br>$ git status<br><br>### stage changes<br>$ git add -A<br><br>### commit the changes<br>$ git commit -m "Second Commit: get the django_remote_forms folder from <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms/&amp;sa=D&amp;ust=1585972458597000" class="c14">https://github.com/sant527/django_remote_forms/</a>"<br><br>### check git log<br>$ git --no-pager log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(green)%s%C(reset) %C(dim magenta)- %an%C(reset)' --all<br><br>### git remote check<br>$ git remote -v<br><br>### push to remote<br>$ git push -f origin master<br><br>### check git log<br>$ git --no-pager log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(green)%s%C(reset) %C(dim magenta)- %an%C(reset)' --all<br></td></tr></tbody></table>

 * ## \[image\] screenshot of terminator for this commit

     * ![](images/image220.png)![](images/image84.png)![](images/image228.png)![](images/image344.png)![](images/image100.png)![](images/image34.png)

 * ## \[code\] Some sample Example

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Minimal Example:<br><br>from django_remote_forms.forms import RemoteForm<br><br>form = LoginForm()<br>remote_form = RemoteForm(form)<br>remote_form_dict = remote_form.as_dict()<br><br>Upon converting the dictionary into JSON, it looks like this:<br><br>{<br>    "is_bound": false,<br>    "non_field_errors": [],<br>    "errors": {},<br>    "title": "LoginForm",<br>    "fields": {<br>        "username": {<br>            "title": "CharField",<br>            "required": true,<br>            "label": "Username",<br>            "initial": null,<br>            "help_text": "This is your django username",<br>            "error_messages": {<br>                "required": "This field is required.",<br>                "invalid": "Enter a valid value."<br>            },<br>            "widget": {<br>                "title": "TextInput",<br>                "is_hidden": false,<br>                "needs_multipart_form": false,<br>                "is_localized": false,<br>                "is_required": true,<br>                "attrs": {<br>                    "maxlength": "30"<br>                },<br>                "input_type": "text"<br>            },<br>            "min_length": 6,<br>            "max_length": 30<br>        },<br>        "password": {<br>            "title": "CharField",<br>            "required": true,<br>            "label": "Password",<br>            "initial": null,<br>            "help_text": "",<br>            "error_messages": {<br>                "required": "This field is required.",<br>                "invalid": "Enter a valid value."<br>            },<br>            "widget": {<br>                "title": "PasswordInput",<br>                "is_hidden": false,<br>                "needs_multipart_form": false,<br>                "is_localized": false,<br>                "is_required": true,<br>                "attrs": {<br>                    "maxlength": "128"<br>                },<br>                "input_type": "password"<br>            },<br>            "min_length": 6,<br>            "max_length": 128<br>        }<br>    },<br>    "label_suffix": ":",<br>    "prefix": null,<br>    "csrfmiddlewaretoken": "2M3MDgfzBmkmBrJ9U0MuYUdy8vgeCCgw",<br>    "data": {<br>        "username": null,<br>        "password": null<br>    }<br>}<br><br></td></tr></tbody></table>

* # Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail

 * ## \[code\] UserLoginViaOtpFormEmail (this already defined)

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/forms.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from custom_user.models import User<br>from django import forms<br>from basic_django import settings<br><br>class UserLoginViaOtpFormEmail(forms.ModelForm):<br>    class Meta:<br>        model = User<br>        fields = ['email']<br><br>    # we can create the email manually, but since its already defined we take advantage from model<br><br>    ############### important whenever for ease we use a field from a model################### <br>    # if we dont call clean. it<br>    #will check for unique instance clause for email  and gives User already exists:<br>    #go to: class BaseModelForm(BaseForm): --- self._validate_unique = False<br>    def clean(self):<br>        return self.cleaned_data<br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image172.png)

 * ## \[code\] api endpoint: api\_user\_login\_via\_otp\_form\_email\_django\_forms\_example

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/views.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.core.serializers.json import DjangoJSONEncoder<br>from django.views.decorators.csrf import csrf_exempt<br>from django.middleware.csrf import CsrfViewMiddleware<br>from django_remote_forms.forms import RemoteForm<br>import json<br>from .forms import UserLoginViaOtpFormEmail<br>from django.http import HttpResponse<br><br><br>@csrf_exempt<br>def api_user_login_via_otp_form_email_django_forms_example(request):<br>    csrf_middleware = CsrfViewMiddleware()<br><br>    response_data = {}<br>    if request.method == 'GET':<br>        # Get form definition<br>        form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL2})<br>    elif request.method == 'POST':<br>        if request.content_type  != 'application/json':<br>            return HttpResponse(json.dumps({"detail": "Unsupported media type \"'%s'\" in request." % request.content_type}), content_type="application/json",status=401);<br>        # Process request for CSRF<br>        csrf_middleware.process_view(request, None, None, None)<br>        form_data = json.loads(request.body)<br>        form = UserLoginViaOtpFormEmail(form_data)<br>        if form.is_valid():<br>            email = form.cleaned_data.get('email')<br>            response = HttpResponse(<br>                {'email': email},<br>                content_type="application/json"<br>            )<br><br>    remote_form = RemoteForm(form)<br>    # Errors in response_data['non_field_errors'] and response_data['errors']<br>    response_data.update(remote_form.as_dict())<br><br>    response = HttpResponse(<br>        json.dumps(response_data, cls=DjangoJSONEncoder),<br>        content_type="application/json"<br>    )<br><br>    # Process response for CSRF<br>    csrf_middleware.process_response(request, response)<br>    return response<br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image214.png)

 * ## \[code\] urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Add to urlpatterns: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/login_register_password/urls.py<br><br>path('api_user_login_via_otp_form_email_django_forms_example',views.api_user_login_via_otp_form_email_django_forms_example,name='api_user_login_via_otp_form_email_django_forms_example')<br></td></tr></tbody></table>

 * ## \[image\] urls.py 

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/urls.py

     * ![](images/image210.png)

 * ## \[image\] output after opening the link 

     * http://localhost:8000/login\_register\_password/api\_user\_login\_via\_otp\_form\_email\_django\_forms\_example

     * ![](images/image106.png)

     * \[code\] Commit the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>## Check git status<br> 19:46:23  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✹<br>$ git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   login_register_password/urls.py<br>        modified:   login_register_password/views.py<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br>## Check git stage changes<br> 19:46:27  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✹<br>$ git add -A<br><br>## Check git commit changes<br> 19:47:21  ✘  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✚<br>$ git commit -m "Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail"<br>[master 58480ed] Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail<br> 2 files changed, 46 insertions(+)<br><br>## push changes<br> 19:48:47  ✘  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✔<br>$ git push origin master                                                                                                            <br>Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>Enumerating objects: 11, done.<br>Counting objects: 100% (11/11), done.<br>Delta compression using up to 4 threads<br>Compressing objects: 100% (6/6), done.<br>Writing objects: 100% (6/6), 1.19 KiB | 1.19 MiB/s, done.<br>Total 6 (delta 5), reused 0 (delta 0)<br>remote: Resolving deltas: 100% (5/5), completed with 5 local objects.<br>remote: <br>remote: GitHub found 1 vulnerability on sant527/django_basic_documentation_ver2's default branch (1 moderate). To find out more, visit:<br>remote:      https://github.com/sant527/django_basic_documentation_ver2/network/alerts<br>remote: <br>To github.com:sant527/django_basic_documentation_ver2.git<br>   56e04e3..58480ed  master -&gt; master<br></td></tr></tbody></table>

* # Third Commit: Add  node\_module to gitignore

     * Since in the next commit we will be setting up npm which will create node\_modules dir which we want to ignore

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 10:32:08  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git status<br>On branch master<br>nothing to commit, working tree clean<br><br>## NOW DO the changes to .gitignore by adding<br><br># node modules npm init<br>node_modules/<br><br><br> 10:32:19  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   .gitignore<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br> 10:33:58  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✹<br>$ git add -A<br><br> 10:34:03  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✚<br>$ git commit -m "Third Commit: Add  node_module to gitignore"<br>[master a12744b] Third Commit: Add  node_module to gitignore<br> 1 file changed, 4 insertions(+)<br><br> 10:34:15  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git push<br>fatal: The current branch master has no upstream branch.<br>To push the current branch and set the remote as upstream, use<br><br>    git push --set-upstream origin master<br><br> 10:34:45  ✘  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git push --set-upstream origin master                             <br>Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>Enumerating objects: 5, done.<br>Counting objects: 100% (5/5), done.<br>Delta compression using up to 4 threads<br>Compressing objects: 100% (3/3), done.<br>Writing objects: 100% (3/3), 409 bytes | 409.00 KiB/s, done.<br>Total 3 (delta 1), reused 0 (delta 0)<br>remote: Resolving deltas: 100% (1/1), completed with 1 local object.<br>remote: <br>remote: GitHub found 1 vulnerability on sant527/django_basic_documentation_ver2's default branch (1 moderate). To find out more, visit:<br>remote:      https://github.com/sant527/django_basic_documentation_ver2/network/alerts<br>remote: <br>To github.com:sant527/django_basic_documentation_ver2.git<br>   58480ed..a12744b  master -&gt; master<br>Branch 'master' set up to track remote branch 'master' from 'origin'.<br></td></tr></tbody></table>

 * ## \[images\] changing .gitignore

     * ![](images/image205.gif)

     * Now add node\_modules to the .gitignore file

     * ![](images/image246.png)

     * Now commit the changes

     * ![](images/image239.png)![](images/image148.png)

* # Fourth Commit: Setup Nodejs project. Install webpack, webpack-bundle-tracker, react, react-dom, @babel/core babel-loader @babel/preset-env @babel/preset-react and django-webpack-loader (python)

     * Shifting to API based development: To develop mobile applications we cant use web based. Rather we provide the data as JSON and then the mobile application displays it. So on web based apps also we will use data from api rather then loading the web page from backed directly. For that we will use ReactJS as out frontend developer.

     * Reactjs: We will use ReactJs as frontend along with the base template. We will supply the data using api. 

     * webpack: is a module bundler. Its main purpose is to bundle JavaScript files for usage in a browser.

     * Django-webpack-loader: Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

     * [https://github.com/owais/django-webpack-loader](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&sa=D&ust=1585972458641000)

     * Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

 * ## Webpack

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Even a simple project contains HTML, CSS and JavaScript files. Also, it can contains assets such as fonts, images, and so on. <br><br>As its core, webpack is a static module bundler. In a particular project, webpack treats all files and assets as modules. Under the hood, it relies on a dependency graph. A dependency graph describes how modules relate to each other using the references (require and import statements) between files. In this way, webpack statically traverses all modules to build the graph, and uses it to generate a single bundle (or several bundles) — a JavaScript file containing the code from all modules combined in the correct order. “Statically” means that, when webpack builds its dependency graph, it doesn’t execute the source code but stitches modules and their dependencies together into a bundle. This can then be included in your HTML files.<br><br>webpack.config.js, which describes how the files and assets should be transformed and what kind of output should be generated.<br><br>Based on the provided configuration, webpack starts from the entry points and resolves each module it encounters while constructing the dependency graph. If a module contains dependencies, the process is performed recursively against each dependency until the traversal has completed. Then webpack bundles all project’s modules into a small number of bundles — usually, just one — to be loaded by the browser.<br></td></tr></tbody></table>

 * ## \[code\] npm init

     * An Absolute Beginner's Guide to Using npm

     * [https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/](https://www.google.com/url?q=https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/&sa=D&ust=1585972458644000)

     * npm (originally short for Node Package Manager) is a package manager for the JavaScript programming language.

     * npm init when you're first creating a project. It essentially just creates the package.json

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>$ npm init<br></td></tr></tbody></table>

 * ## \[image\] npm init

     * ![](images/image177.png)![](images/image39.png)

 * ## \[code\] Npm: Install webpack and webpack-bundle-tracker

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>WEBPACK RELATED:<br>webpack: we will need webpack package<br><br>Webpack-bundle-tracker: plugin to extract useful information from webpack and store it in as json in a file. This file will act as the link between webpack and django.<br><br>Installation:<br>npm install --save-dev webpack webpack-bundle-tracker webpack-cli<br></td></tr></tbody></table>

     * We have to config webpack by webpack.config.js  and also use the plugins BundleTracker. This will show later

     * Eg: just for mention about BundleTracker plugin inside webpack.config.js

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var BundleTracker = require('webpack-bundle-tracker');<br><br>module.exports = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './src/webpack-stats.json'}),<br>  ],<br>}<br></td></tr></tbody></table>

     * Also after installing django-webpack-loader python package we have to add to the settings.py

     * Settings.py (just for mention)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>STATIC_URL = '/static/'<br><br>WEBPACK_LOADER = {<br>    'DEFAULT': {<br>        'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.<br>        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>        # '/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/webpack-stats.json'<br>    }<br>}<br></td></tr></tbody></table>

 * ## \[code\] npm : Install reactjs and babel

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>REACTJS RELATED:<br>React: Reactjs is a JavaScript library to build UI and is one of the widely used and popular JavaScript library in today’s date.<br><br>React-dom: We will be needing one more package called react-dom package to render the DOM.<br><br>Installation:<br>npm install --save-dev react react-dom<br><br>BABEL RELATED:<br>babel-core: babel transpile ES6 code to ES5<br><br>babel-loader: This is a webpack helper which allows to transpile Javascript files with babel and webpack. It uses babel under the hood<br><br>babel/preset-env: It determines which features needs to be transformed to run within different browsers or runtime versions. This is also known as browser polyfills<br><br>babel/preset-react: It is used to transform all your React JSX into functions.<br><br>Installation: <br>npm install --save-dev @babel/core babel-loader @babel/preset-env @babel/preset-react<br></td></tr></tbody></table>

 * ## \[image\] npm: package.json

     * ![](images/image261.png)![](images/image312.png)

 * ## \[code\] .Babelrc for reactjs and  babel-loader to webpack.config.js \[this is done in next commit. But shown here also\]

     * We also need to setup our babel config file, create a new file in the root directory called .babelrc and write the following configuration to it

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br>Touch .babelrc<br></td></tr></tbody></table>

     * .babelrc

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>  "presets": ["@babel/preset-env", "@babel/preset-react"]<br>}<br><br></td></tr></tbody></table>

     * The above configuration will ensure that babel transpiles our react code, which is JSX and any other ES6+ code we have to ES5 code.

     * Add the babel-loader to webpack.config.js

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>module.exports = {<br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  }<br>}<br></td></tr></tbody></table>

     * What the above configuration does is that for every file with a js or jsx extension, excluding the node\_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. With this done, lets head over to writing our react component.

     * https://scotch.io/@deityhub/settingup-reactjs-using-webpack-4-and-babel-7-the-definitive-guide

 * ## \[code\] pipenv: install django-webpack-loader

     * Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

     * |                                                              |

     * | ------------------------------------------------------------ |

     * | pipenv install django-webpack-loader |

 * ## \[code\] Create empty webpack.config.js and .babelrc files

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 10:41:12  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔ ⬆<br>$ touch webpack.config.js<br><br> 10:42:13  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ⬆ ✭<br>$ touch .babelrc<br><br> 10:59:42  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ⬆ ✹ ✭<br>$ git add -A<br><br>$ git commit -m "Fourth Commit: Setup Nodejs project. Install webpack, webpack-bundle-tracker, react, react-dom, @babel/core babel-loader @babel/preset-env @babel/preset-react and django-webpack-loader (python)"<br><br><br></td></tr></tbody></table>

 * ## \[images\] npm init and install webpack, react, babel and django-webpack

     * ![](images/image262.png)![](images/image164.png)![](images/image319.png)![](images/image117.png)

* # FIFTH COMMIT: Setup webpack.config.js, babelrc and settings.py 

     * Also after installing django-webpack-loader python package we have to add to the settings.py

 * ## \[code\] Add webpack\_loader to INSTALLED\_APPS

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INSTALLED_APPS = (<br>    ...<br>    'webpack_loader',<br>)<br></td></tr></tbody></table>

 * ## \[code\] configuring django-webpack-loader in settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>WEBPACK_LOADER = {<br>    'DEFAULT': {<br>        'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.<br>        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>        #BASE_DIR is your Django project directory. The same directory where manage.py is located.<br>    }<br>}<br></td></tr></tbody></table>

 * ## \[images\] diff file

     * ![](images/image195.png)![](images/image66.png)

 * ## \[code\] webpack.config.js

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>NOT SINGLE PAGE APP:<br>We are not creating single page APP. We will have separate .js file for each view<br><br>We will configure our webpack in such a way that it will have different entry points and output points.<br>MULTIPLE ENTRIES<br>For having multiple entry points we have to mention the path in the key name<br>The entry name should be the similar to the django notatio<br><br>BEFORE:<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br><br>AFTER:<br>                        ├── static<br>                        │   └── polls<br>                        │       └── js<br>                        │           ├── bundles<br>                        │           │   ├── index-8ea5b4e40178f2c800ee.js<br>                        │           │   └── question-8ea5b4e40178f2c800ee.js<br>                        │           ├── index.js<br>                        │           └── questions.js<br><br>So example:<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br><br><br>And mention the root folder for output.<br><br>MULTIPLE OUTPUTS<br>For having mutliple outputs we have to use array of configs.<br><br>Example:<br><br>module.exports =[<br>        {<br>          name: "polls",<br>          context: common.context,<br>          entry: entry_output1.entry,<br>          output: entry_output1.output,<br>          plugins: common.plugins,<br>          module: common.module,<br>          resolve: common.resolve,<br>        },<br>           {<br>          name: "login",<br>          context: common.context,<br>          entry: entry_output2.entry,<br>          output: entry_output2.output,<br>          plugins: common.plugins,<br>          module: common.module,<br>          resolve: common.resolve,             <br>           }<br><br>]<br><br>And entry_output1 is:<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br><br><br>And common is:<br><br>common = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var path = require("path");<br>var webpack = require('webpack');<br>var BundleTracker = require('webpack-bundle-tracker');<br><br><br>//the below are the common properties<br>common = {<br>  context: __dirname,<br><br><br>  /* PLUGINS NOTE:<br>  we have installed webpack-bundle-tracker.  npm install --save-dev webpack webpack-bundle-tracker. So we have to add this to the configuration <br>  filename will reside where manager.py resides<br>  Because: django-webpack-loader (python) package setttings.py we set the path as below<br><br>  WEBPACK_LOADER = {<br>      'DEFAULT': {<br>          'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.<br>          'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>          #BASE_DIR is your Django project directory. The same directory where manage.py is located.<br>      }<br>  }<br>  Form above we have to ensure the absolute path of webpack-stats.json is same as os.path.join(BASE_DIR, 'webpack-stats.json')<br>  */<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  /* MODULE Note<br>  we have installed babel-loader: This is a webpack helper which allows to transpile Javascript files with babel and webpack. It uses babel under the hood<br>  What the below configuration does is that for every file with a js or jsx extension, excluding the node_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. <br>  */<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  /* RESOLVE NOTE<br>  Webpack uses resolve.extensions to generate all the possible paths to the module, e.g.<br><br>  function getPaths(module) {<br>      return ['', '.js', '.css'].map(ext =&gt; module + ext);<br>  }<br><br>  getPaths('./somefile'); // ['./somefile', './somefile.js', './somefile.css']<br><br>  getPaths('./somefile.js'); // ['./somefile.js', './somefile.js.js', './somefile.js.css']<br><br>  Webpack would then proceed to lookup each of those paths until it finds a file.<br>  */<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br><br>/* ENTRY OUTPUT EXAMPLE NOTE<br>Example entry ouput object which will be used in the array for module exports<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br>*/<br><br><br>/* MODULE EXPORTS ARRAY NOTE<br> Why are we using array. Because we want different output folders which is not possible<br> with single object<br>*/<br><br>module.exports = [<br>  {<br>    name: "somename",<br>    context: common.context,<br>// Here fill the entry_output<br>/*    entry: entry_output1.entry,<br>    output: entry_output1.output,*/<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,<br>  }<br>]<br><br><br><br><br><br>/* HOW MULTIPLE ENTRY AND OUTPUT WORK NOTE<br>How to set multiple file entry and output in project with webpack?<br>Webpack: path as the entry name: <br><br>EG:<br>pwd: /home/user/project/<br><br>Tree -A<br><br>apps<br>├── dir1<br>│   └── js<br>│       ├── main.js [entry 1]<br>│       └── bundle.js [output 1]<br>└── dir2<br>    ├── index.js [entry 2]<br>    └── foo.js [output 2]<br><br> <br>NOTE dont use / in path.resolve i.e apps/dir1/js/main.js is right /apps/dir1/js/main.js is wrong<br>ERROR in Entry module not found: Error: Can't resolve '/basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js' in '/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2'<br><br>{<br>  entry: {<br>    'dir1/js/bundle': path.resolve(__dirname, 'apps/dir1/js/main.js'),<br>    'dir2/foo' : path.resolve(__dirname, 'apps/dir2/index.js')<br>  },<br>  output: {<br>    path: path.resolve(__dirname, 'apps'),  i.e /home/user/project/apps<br>    filename: '[name]-[hash].js'<br>  },<br>  ...<br>}<br><br>Here  'dir1/js/bundle' is [name] of the entry point. <br><br>Here the important thing is [name] and path  (Use [name] to get the name of the entry point)<br><br>Its like <br>[path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name]-[hash].js'<br>] == [full path]+[name]-[hash].js  == [/home/user/project/apps/]+[dir1/js/bundle]-[jhajkhkd].js = /home/user/project/apps/dir1/js/bundle-jhajkhkd.js<br><br><br>and then stats file become:<br><br>{<br>  "status": "done",<br>  "chunks": {<br><br>    # this is same as the entry name<br>    "dir1/js/bundle": [<br>      {<br><br>        # here name is derived from filename: '[name]-[hash].js' ([name] is entry index name)<br>        "name": "dir1/js/bundle-jhajkhkd.js",<br><br>        # here path is derived from [full path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name].js'] = [path] + [name].js <br>        "path": "/home/user/project/apps/dir1/js/bundle-jhajkhkd.js"<br><br>      }<br>    ],<br>    "dir2/foo": [<br>      {<br>        "name": "dir2/foo.js",<br>        "path": "/home/user/project/apps/dir2/foo-hgjhghjg.js"<br>      }<br>    ]<br>  }<br>}<br><br><br>ALSO ANOTHER EXAMPLE:<br><br><br>NOT SINGLE PAGE APP:<br>We are not creating single page APP. We will have separate .js file for each view<br><br>We will configure our webpack in such a way that it will have different entry points and output points.<br>MULTIPLE ENTRIES<br>For having multiple entry points we have to mention the path in the key name<br>The entry name should be the similar to the django notatio<br><br>BEFORE:<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br><br>AFTER:<br>                        ├── static<br>                        │   └── polls<br>                        │       └── js<br>                        │           ├── bundles<br>                        │           │   ├── index-8ea5b4e40178f2c800ee.js<br>                        │           │   └── question-8ea5b4e40178f2c800ee.js<br>                        │           ├── index.js<br>                        │           └── questions.js<br><br>So example:<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br><br><br>And mention the root folder for output.<br><br>MULTIPLE OUTPUTS<br>For having mutliple outputs we have to use array of configs.<br><br>Example:<br><br>module.exports =[<br>  {<br>    name: "polls",<br>    context: common.context,<br>    entry: entry_output1.entry,<br>    output: entry_output1.output,<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,<br>  },<br>           {<br>    name: "login",<br>    context: common.context,<br>    entry: entry_output2.entry,<br>    output: entry_output2.output,<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,             <br>           }<br><br>]<br><br>And entry_output1 is:<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br><br><br>And common is:<br><br>common = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br><br>*/<br><br></td></tr></tbody></table>

 * ## \[image\] webpack config

     * ![](images/image119.png)![](images/image101.png)![](images/image200.png)![](images/image193.png)![](images/image127.png)![](images/image159.png)![](images/image245.png)![](images/image150.png)![](images/image340.png)

 * ## \[code\] .Babelrc for reactjs and  babel-loader(already added above but just shown) to webpack.config.js 

     * We also need to setup our babel config file, create a new file in the root directory called .babelrc and write the following configuration to it

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br>Touch .babelrc (we have already created .babelrc in the previous commit)<br></td></tr></tbody></table>

     * .babelrc

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>  "presets": ["@babel/preset-env", "@babel/preset-react"]<br>}<br><br></td></tr></tbody></table>

     * The above configuration will ensure that babel transpiles our react code, which is JSX and any other ES6+ code we have to ES5 code.

 * ## \[image\] .babelrc

     * ![](images/image264.png)

     * Add the babel-loader to webpack.config.js (this is just for reference. Its already included in the above (webpack.config.js)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>module.exports = {<br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  }<br>}<br></td></tr></tbody></table>

     * What the above configuration does is that for every file with a js or jsx extension, excluding the node\_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. With this done, lets head over to writing our react component.

     * https://scotch.io/@deityhub/settingup-reactjs-using-webpack-4-and-babel-7-the-definitive-guide

 * ## \[code\] git staging and commiting the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ git add -A<br><br> 11:06:37  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ⬇ ⬆ ✚<br>$ git commit -m "FIFTH COMMIT: Setup webpack.config.js, babelrc and settings.py"<br><br> 11:07:02  ✘  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔ ⬇ ⬆<br>$ git push -f origin master <br></td></tr></tbody></table>

* # Sixth Commit: Compiling bundles using webpack and watch mode

 * ## \[code\] Compiling our bundle using webpack.config.js

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Binaries shipped with node packages are installed to node_modules/.bin/ and it not added to $PATH automatically so we need to use full paths to the binaries.<br><br>./node_modules/.bin/webpack --config webpack.config.js<br></td></tr></tbody></table>

     * This should create bundle at the \[path\]+\[filename\]. This is good but we don’t want to create bundles manually every time we make changes to our code.

 * ## \[code\] Watch mode for webpack.config.js:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ ./node_modules/.bin/webpack --config webpack.config.js --watch<br></td></tr></tbody></table>

     * This will leave the compiler running and compile bundles automatically when you change any of your source files. You’ll need to restart it if you make any changes to the webpack configuration though.

* # Seventh Commit - A: Example of webpack and Reactjs:: Getting polls app

 * ## \[code\] Go to the project folder (where .manage.py resides)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django<br></td></tr></tbody></table>

 * ## \[code\] get the polls folder from github

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ svn ls https://github.com/sant527/polls_example_for_webpack_and_reactjs.git<br>branches/<br>trunk/<br><br>$ svn ls https://github.com/sant527/polls_example_for_webpack_and_reactjs.git/trunk<br>.gitignore<br>README.md<br>polls_example_for_webpack_and_reactjs/<br><br>$ svn export https://github.com/sant527/polls_example_for_webpack_and_reactjs.git/trunk/polls_example_for_webpack_and_reactjs<br></td></tr></tbody></table>

 * ## \[code\] Commit the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 18:17:36  ⚙ simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django   master ✘ ✚<br>$ git add -A                                                                        <br><br> 18:17:42  ✘ ⚙  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django   master ✘ ✚<br>$ git commit -m "Seventh Commit - A: Example of webpack and Reactjs:: Getting polls app"<br><br> 18:18:03  ⚙ simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django   master ✔ ⬆<br>$ git push<br></td></tr></tbody></table>

* # Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app

 * ## \[code\] Add polls\_example\_for\_webpack\_and\_reactjs.polls to the installed INSTALLED\_APPS

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Eg:<br><br>INSTALLED_APPS = [<br>    'django.contrib.admin',<br>    'django.contrib.auth',<br>    'django.contrib.contenttypes',<br>    'django.contrib.sessions',<br>    'django.contrib.messages',<br>    'django.contrib.staticfiles',<br>    'polls_example_for_webpack_and_reactjs.polls'<br>]<br></td></tr></tbody></table>

 * ## \[code\] Then make the migrations

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 18:29:25  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 DO_NOT_DELETE_djang_basic_documentation_pa-kHaUQTsF   master ✘ ✹<br>$ python manage.py makemigrations<br>Migrations for 'custom_user':<br>  custom_user/migrations/0004_auto_20191222_1300.py<br>    - Alter field password on user<br>Migrations for 'polls':<br>  polls_example_for_webpack_and_reactjs/polls/migrations/0001_initial.py<br>    - Create model Question<br>    - Create model Choice<br><br><br> 18:30:25  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 DO_NOT_DELETE_djang_basic_documentation_pa-kHaUQTsF   master ✘ ✹ ✭<br>$ python manage.py migrate       <br>Operations to perform:<br>  Apply all migrations: admin, auth, contenttypes, custom_user, polls, sessions<br>Running migrations:<br>  Applying custom_user.0004_auto_20191222_1300... OK<br>  Applying polls.0001_initial... OK<br></td></tr></tbody></table>

 * ## \[code\] Providing initial data for polls models

     * Here we are providing data using fixtures file: https://docs.djangoproject.com/en/3.0/howto/initial-data/\#providing-data-with-fixtures

     * Its just a json file lying inside a folder called fxitures inside the app

     * Here it is polls\_example\_for\_webpack\_and\_reactjs/polls/fixtures/poll\_database.json

     * We have created some initial data to pass and test. To add that to database just do

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 18:55:38  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 DO_NOT_DELETE_djang_basic_documentation_pa-kHaUQTsF   master ✘ ✹ ✭<br>$ python manage.py loaddata poll_database.json<br>Installed 8 object(s) from 1 fixture(s)<br></td></tr></tbody></table>

 * ## \[code\] Then add to the webpack.config.js the paths of the ReactJs files

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> <br>var path = require("path");<br>var webpack = require('webpack');<br>var BundleTracker = require('webpack-bundle-tracker');<br><br><br>common = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br><br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br><br><br>module.exports =[<br>        {<br>          name: "polls",<br>          context: common.context,<br>          entry: entry_output1.entry,<br>          output: entry_output1.output,<br>          plugins: common.plugins,<br>          module: common.module,<br>          resolve: common.resolve,<br>        }<br><br>]<br><br>/*<br>Before:<br>home<br>└── web_dev<br>    └── DO_NOT_DELETE_djang_basic_documentation_part2<br>        └── basic_django<br>            └── polls_example_for_webpack_and_reactjs<br>                ├── __init__.py<br>                ├── hare.py<br>                ├── models.py<br>                └── polls<br>                    ├── __init__.py<br>                    ├── admin.py<br>                    ├── apps.py<br>                    ├── fixtures<br>                    ├── migrations<br>                    ├── models.py<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br>                    ├── templates<br>                    ├── tests.py<br>                    ├── urls.py<br>                    └── views.py<br><br><br>AFTER*******************************<br><br> 19:38:00  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✹ ✭<br>$ tree --noreport --fromfile &lt;&lt;EOF                      <br>`tree -f -i -n -F --noreport /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/polls_example_for_webpack_and_reactjs | grep -E -v 'templates/.+|migrations/.+|fixtures/.+|^\.$'`<br>EOF<br>.<br>└── home<br>    └── web_dev<br>        └── DO_NOT_DELETE_djang_basic_documentation_part2<br>            └── basic_django<br>                └── polls_example_for_webpack_and_reactjs<br>                    ├── __init__.py<br>                    ├── hare.py<br>                    ├── models.py<br>                    └── polls<br>                        ├── __init__.py<br>                        ├── admin.py<br>                        ├── apps.py<br>                        ├── fixtures<br>                        ├── migrations<br>                        ├── models.py<br>                        ├── static<br>                        │   └── polls<br>                        │       └── js<br>                        │           ├── bundles<br>                        │           │   ├── index-8ea5b4e40178f2c800ee.js<br>                        │           │   └── question-8ea5b4e40178f2c800ee.js<br>                        │           ├── index.js<br>                        │           └── questions.js<br>                        ├── templates<br>                        ├── tests.py<br>                        ├── urls.py<br>                        └── views.py<br><br><br>*/<br><br><br>// How to run it<br>/*<br><br>$ ./node_modules/.bin/webpack --config webpack.config.js<br>Hash: f321a5521d75ab142c8c<br>Version: webpack 4.41.3<br>Child polls:<br>    Hash: f321a5521d75ab142c8c<br>    Time: 1189ms<br>    Built at: 12/23/2019 6:28:19 PM<br>                                              Asset     Size  Chunks                         Chunk Names<br>       /polls/bundles/index-f321a5521d75ab142c8c.js  128 KiB       0  [emitted] [immutable]  /polls/bundles/index<br>    /polls/bundles/question-f321a5521d75ab142c8c.js  130 KiB       1  [emitted] [immutable]  /polls/bundles/question<br>    Entrypoint /polls/bundles/index = /polls/bundles/index-f321a5521d75ab142c8c.js<br>    Entrypoint /polls/bundles/question = /polls/bundles/question-f321a5521d75ab142c8c.js<br>    [7] ./basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js 280 bytes {0} [built]<br>    [8] ./basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js 3.32 KiB {1} [built]<br>        + 7 hidden modules<br>    <br>    WARNING in configuration<br>    The 'mode' option has not been set, webpack will fallback to 'production' for this value. Set 'mode' option to 'development' or 'production' to enable defaults for each environment.<br>    You can also set it to 'none' to disable any default behavior. Learn more: https://webpack.js.org/configuration/mode/<br><br> 18:28:20  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✹ ✭<br>$ <br><br>webpack-stats.json<br>{<br>  "status": "done",<br>  "chunks": {<br>    "/polls/bundles/index": [<br>      {<br>        "name": "/polls/bundles/index-f321a5521d75ab142c8c.js",<br>        "path": "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/bundles/index-f321a5521d75ab142c8c.js"<br>      }<br>    ],<br>    "/polls/bundles/question": [<br>      {<br>        "name": "/polls/bundles/question-f321a5521d75ab142c8c.js",<br>        "path": "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/bundles/question-f321a5521d75ab142c8c.js"<br>      }<br>    ]<br>  }<br>}<br><br>*/<br><br>// normal js<br><br>// for(var k in firstObject) secondObject[k]=firstObject[k];<br><br>// ES6 spread operator<br>// //const thirdObject = {<br>//    ...firstObject,<br>//    ...secondObject   <br>// }<br>// Works in Chrome, this is ES6, you will need Babel or some ES6 transpiler currently. In the future all browser are expected to support this syntax.<br><br><br></td></tr></tbody></table>

 * ## \[images\] webpack.config.js

     * ![](images/image81.png)![](images/image305.png)![](images/image229.png)![](images/image133.png)![](images/image350.png)![](images/image125.png)

 * ## \[code\] Generate the bundle js using webpack and runserver and check whether the reactjs is working

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ Cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br>$ ./node_modules/.bin/webpack --config webpack.config.js<br>$ cd basic_django<br>$ python manage.py runserver <br><br>localhost:8000/polls_webpack_react_example<br>localhost:8000/polls_webpack_react_example/questions<br></td></tr></tbody></table>

 * ## \[image\] generate bundle and runserver and check urls

     * ![](images/image224.png)![](images/image65.png)

 * ## \[code\] Then add to the urls of of the project

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/basic\_django/urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib import admin<br>from django.urls import path, include<br><br>urlpatterns = [<br>…<br>    path('polls_webpack_react_example/', include('polls_example_for_webpack_and_reactjs.polls.urls')),<br>...<br>]<br></td></tr></tbody></table>

 * ## \[code\] After starting the server open the links:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>localhost:8000/polls_webpack_react_example<br>localhost:8000/polls_webpack_react_example/questions<br></td></tr></tbody></table>

 * ## \[code\] commit changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 23:16:41  ⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 DO_NOT_DELETE_djang_basic_documentation_pa-kHaUQTsF   master ✘ ⬇ ⬆ ✚<br>$ git status<br>On branch master<br>Your branch and 'origin/master' have diverged,<br>and have 3 and 3 different commits each, respectively.<br>  (use "git pull" to merge the remote branch into yours)<br><br>Changes to be committed:<br>  (use "git reset HEAD &lt;file&gt;..." to unstage)<br><br>        modified:   basic_django/basic_django/settings.py<br>        modified:   basic_django/basic_django/urls.py<br>        new file:   basic_django/custom_user/migrations/0004_auto_20191222_1300.py<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/migrations/0001_initial.py<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/index-ff981c23bdb4b0ef93e3.js<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/questions-ff981c23bdb4b0ef93e3.js<br>        new file:   basic_django/webpack-stats.json<br>        modified:   package-lock.json<br>        modified:   package.json<br>        modified:   webpack.config.js<br><br><br>$ git commit -m "Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app"<br>[master f603b9c] Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app<br> 10 files changed, 762 insertions(+), 46 deletions(-)<br> create mode 100644 basic_django/custom_user/migrations/0004_auto_20191222_1300.py<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/migrations/0001_initial.py<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/index-ff981c23bdb4b0ef93e3.js<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/questions-ff981c23bdb4b0ef93e3.js<br> create mode 100644 basic_django/webpack-stats.json<br><br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image281.png)

* # EIGHT COMMIT: JWT TOKEN AUTHENTICATION

     * Pyjwt package is used to create a token and also decode a token

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Creating a token<br><br>jwt.encode(<br>        payload,<br>        key,<br>        algorithm<br>    )<br><br><br>Decoding a token:<br><br>jwt.decode(<br>        token,<br>        secret_key<br>        api_settings.JWT_VERIFY,<br>        options=options,<br>        leeway=api_settings.JWT_LEEWAY,<br>        audience=api_settings.JWT_AUDIENCE,<br>        issuer=api_settings.JWT_ISSUER,<br>        algorithms=[api_settings.JWT_ALGORITHM]<br>    )<br><br><br></td></tr></tbody></table>

 * ## \[code-install\] Install django-rest-framework

     * We will be using the functions from rest\_framework\_jwt. But we will use them customizing as per out needs. Also we have to install django rest framework for we will be using exceptions from it

     * |                                                              |

     * | ------------------------------------------------------------ |

     * | Pipenv install django-rest-framework |

     * Then the following are the functions and theory which will be used to work with jwt:

     * A file called understanding\_jwt\_authentication.py is created in the project root which shows the code etc

 * ## \[images\] jwt procedure and functions

     * ![](images/image215.png)![](images/image82.png)![](images/image223.png)![](images/image300.png)![](images/image72.png)![](images/image141.png)![](images/image187.png)![](images/image252.png)![](images/image11.png)![](images/image13.png)![](images/image179.png)![](images/image3.png)

* # EIGHT B : Creating views to login using OTP with token method:

 * ## \[code - install\] postman

     * Install postman-bin from aur [https://aur.archlinux.org/packages/postman-bin/](https://www.google.com/url?q=https://aur.archlinux.org/packages/postman-bin/&sa=D&ust=1585972458867000)

 * ## \[code - commands \] Mkdir api inside login\_register\_password

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd login_register_password<br>Mkdir api<br>Touch views.py<br></td></tr></tbody></table>

 * ## \[code - install\]  Django request logging

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Pipenv install django-request-logging<br><br>Add these to settings.py<br><br>if DEBUG:<br>    MIDDLEWARE += [<br>    'querycount_mod.middleware.QueryCountMiddleware'<br>    # added from django-request-logging<br>    'request_logging.middleware.LoggingMiddleware',<br>    ]<br><br><br><br>        # added from django-request-logging<br>        'django.request': {<br>            'handlers': ['console'],<br>            'level': logging.CRITICAL if DEBUG else 'INFO',  # change debug level as appropiate<br>            'propagate': False,<br>        },<br><br>    }<br>}<br><br># added from django-<br>REQUEST_LOGGING_DATA_LOG_LEVEL=logging.CRITICAL<br>REQUEST_LOGGING_HTTP_4XX_LOG_LEVEL=logging.CRITICAL<br><br></td></tr></tbody></table>

     * [https://stackoverflow.com/a/32017362/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/32017362/2897115&sa=D&ust=1585972458873000)

     * ![](images/image78.png)

     * [https://github.com/Rhumbix/django-request-logging](https://www.google.com/url?q=https://github.com/Rhumbix/django-request-logging&sa=D&ust=1585972458873000)

     * ![](images/image232.png)

 * ## \[code\] downgrade redis to redis==3.3.11 for TypeError: unhashable type: 'Redis'

     * [https://github.com/celery/kombu/issues/1153](https://www.google.com/url?q=https://github.com/celery/kombu/issues/1153&sa=D&ust=1585972458874000)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ pipenv install redis==3.3.11<br></td></tr></tbody></table>

 * ## \[theory\] JWT’s Structure:

     * JSON Web Token comprises 3 strings separated by “.” as follows where each part is encoded with base64url encoding :

     * “eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjp7ImlkIjoiNTlhZDFmZTI0MDVkNzk0YTFkYWQ2YmFkIiwiZGlzcGxheV9uYW1lIjoiQWRtaW4iLCJyb2xlX3R5cGUiOiJhZG1pbiJ9LCJpZCI6IlwiNTliYmJjODc0MDVkNzk0NjYwNGEzZjUyXCIiLCJlbWFpbCI6Imp5b3RpZ2F1dGFtMTA4QGdtYWlsLmNvbSJ9.oGA-goFi7ee6DdKn0Z4sctomaY6Ki0mfuJfxT4OK9WA”

     * ![](images/image87.jpg)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>JWT in short is :- encoded(header)+encoded(payload)+signature(that is already encoded)<br><br>var encoded_string = base64URLEncode(header)+”.”+base64URLEncode(payload)<br>Signature = HMACSHA256(encoded_string,”SECRET”)<br></td></tr></tbody></table>

     * ![](images/image234.png)

 * ## \[code - example\] Creating JSON Web token in python :-

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>First we have to install Python pyjwt library and then using pyjwt:<br><br>&gt;&gt;&gt; import jwt<br>&gt;&gt;&gt; encoded_token = jwt.encode({‘user_id’: “abc”}, ‘SECRET’, algorithm=’HS256')<br>&gt;&gt;&gt; encoded_token<br>‘eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWJjIn0.OW6BZboviYgO6Yy_UTj5jloba7WlPwZnKHPYDUyY3MU’<br><br>Decoding the above created token on server:<br><br>&gt;&gt;&gt; jwt.decode(encoded_token, ‘SECRET’, algorithms=[‘HS256’])<br>{’user_id’: ’abc’}<br></td></tr></tbody></table>

     * Eg: User and Passwd

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>            payload = {<br>                'id': user.id,<br>                'email': user.email,<br>            }<br>            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}<br><br>           return HttpResponse(<br>              json.dumps(jwt_token),<br>              status=200,<br>              content_type="application/json"<br>            )<br><br>ELSE<br />       else:<br>            return HttpResponse(<br>              json.dumps({'Error': "Invalid credentials"}),<br>              status=400,<br>              content_type="application/json"<br>            )<br><br></td></tr></tbody></table>

 * ## Create user\_login\_via\_otp\_form\_email() method in views.py

     * ### \[code\]Basic basic\_django/login\_register\_password/api/views.py/user\_login\_via\_otp\_form\_email()

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>@csrf_exempt<br>def user_login_via_otp_form_email(request):<br>    response_data = {}<br>    if request.method == 'GET':<br>        # Get form definition<br>        form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>    elif request.method == 'POST':<br>        form_data = json.loads(request.body)<br>        logger_custom_string.debug(settings_basic_django.pp_odir(form_data,traceback.format_stack(limit=5)))<br>        form = UserLoginViaOtpFormEmail(form_data)<br>    html = "&lt;html&gt;&lt;body&gt;API TESTING&lt;/body&gt;&lt;/html&gt;"<br>    return HttpResponse(html)<br></td></tr></tbody></table>

       * ![](images/image38.png)

 * ## \[code\] Add to basic\_django/login\_register\_password/api/urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path, include<br>from . import views<br><br>app_name='login_register_password_api_app_name'<br><br>urlpatterns = [<br>    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email')<br>]<br></td></tr></tbody></table>

     * ![](images/image188.png)

     * ### Also add the api urls to the basic\_django/login\_register\_password/urls.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>    # include all the urls from api<br>    path('api/', include('login_register_password.api.urls',namespace='login_register_password_api_app_name')),<br></td></tr></tbody></table>

       * ![](images/image7.png)

 * ## \[code + image\] curl - Test the api url

     * ![](images/image181.png)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ curl --location --request POST 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_email' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"email":"test@test.com"<br>}'<br></td></tr></tbody></table>

     * ![](images/image276.png)

 * ## \[Code\] Create OTP using pyOTP

     * ### Add to settings.py

     * ### \[code settings.py\]

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># SECURITY WARNING: keep the secret key used in production secret!<br>SECRET_KEY_BASE32_PYOTP = env('SECRET_KEY_BASE32_PYOTP')<br><br>#Note: We want to have a common secret separate for OTP instead of using the django secret because if we change the OTP common secret it will then can stop someone misusing the  OTP. Because django_secret is used in many other place. So we dont want to disturb the other secrets<br><br># TIMELIMIT USED FOR pyotp and also jwt<br>TIMELIMIT_OTP = 1200<br></td></tr></tbody></table>

     * ### \[image settings.py\]

       * ![](images/image218.png)

     * ### \[image - generate OTP and corresponding nonce\]

       * ![](images/image306.png)![](images/image303.png)

     * ### \[code  - generate OTP and corresponding nonce\]

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># the following function will generate a pin using pyOTP and also a nonce<br>def generate_pin_pyopt():<br>    ### trying to generate a TOTP (time based One time password)<br>    # we create a nonce (number used once)<br>    # There three ways to create nonce<br>    #1) secrets.token_urlsafe() (we use this)<br>    #2) uuid.uuid4()<br>    #3) str(int(time.time()*1000))<br><br>    nonce = secrets.token_urlsafe()<br><br>    # we use pyotp to generate OTP based on current system time<br>    # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>    # followed by 2–7. 0 and 1 are skipped due to their similarity<br>    # with the letters O and I<br>    # we store the common secret in .env file<br>    base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br><br>    django_secret = settings_basic_django.SECRET_KEY<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br><br>    # Now convert the nonce to base32<br>    # nonce.encode("UTF-8") - converts to bytes<br>    # base64.b32encode() gives byte string<br>    # .decode('utf-8') converts the byte string to string<br>    nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br><br>    django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br><br>    # the final secret we will use in pyotp is combination of<br>    # nonce_base32 + django_secret_base32 + base32_secret<br>    pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>    pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br><br>    pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(),traceback.format_stack(limit=5)))<br>    return pin, nonce<br><br></td></tr></tbody></table>

 * ## Philosophy behind the OTP creation and verification:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#To generate an OTP which is valid till 60s<br>pyotp.TOTP(secret,interval=60).now()<br><br># We want the TOTP to be different even within that 60s<br><br># So the only option to change the OTP is change the secret<br><br># Secret (should be base 32)<br>secret = django secret (convert to base32) + common secret only for OTP (base 32) + nonce (convert to base32)<br><br>We want to have a common secret separate for OTP instead of using the django secret because if we change the OTP common secret it will then can stop someone misusing the  OTP. Because django_secret is used in many other place. So we dont want to disturb the other secrets<br><br>#Nonce - is unique number used once<br>nonce = secrets.token_urlsafe()<br><br>## convert nonce to base32 <br># Now convert the nonce to base32<br># nonce.encode("UTF-8") - converts to bytes<br># base64.b32encode() gives byte string<br># .decode('utf-8') converts the byte string to string<br>nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br><br># Also convert django secret to base32<br><br><br>Now we have to email the OTP<br><br>Send the nonce and email as a jwt_token in the response:<br><br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br><br>SO to verify the OTP, the user has to pass the OTP he recieved from the email and also the jwt_token which contains the email and nonce<br><br><br>Checking OTP:<br>otp_loginconfirm = form.cleaned_data.get('otp_loginconfirm')<br>nonce = payload['nonce']<br><br>Make the secret using the nonce:<br>secret = django secret (convert to base32) + common secret only for OTP (base 32) + nonce (convert to base32)<br><br>Get the pin:<br>pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br><br>Check the pin with OTP submitted with form i.e otp_loginconfirm<br><br></td></tr></tbody></table>

 * ## \[code\] user\_login\_via\_otp\_form\_email 

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/api/views.py

     * ### \[image\] Basic structure

       * ![](images/image57.png)![](images/image314.png)![](images/image194.png)

 * ## Philosophy behind the api creation w.r.t messages and redirect:

     * |                                                                                                                                                                                                                     |

     * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

     * | In api we dont redirect. Every url has to be called individually the reason is, its not like session. Here we want some data to be used in the redirect which the client has to store first |

     * We want to keep the flow of api and the normal view in the same type. The main difference comes in how we handle redirects and also the messages

     * Here messages\_redirect are the messages we want to show in the redirect page. Generally in the session based the messages are stored in the database in the session table.

     * But in the api we cant do that. So we have to pass the data to the client before the redirect. The client will store the data and then when he will show it along with the corresponding redirect url response

     * ![](images/image257.png)

     * Here after the email is posted, otp is created and then its redirected to OTP form. IN the otp form we have to show the message the email is sent

     * ![](images/image335.png)

 * ## 4xx vs 5xx http codes in rest api

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>https://stackoverflow.com/questions/38847441/django-exception-handling-best-practice-and-sending-customized-error-message<br><br>    Usually 4xx errors (Errors that are attributed to the client-side) are disclosed so the user may correct the request.<br />4xx codes are used to tell the client that a fault has taken place on THEIR side. They should not retransmit the same request again, but fix the error first.<br><br>    On the other side, 5xx errors (Errors that are attributed to the server-side) are usually only presented without information. In my opinion for those you should use tools like Sentry do monitor and resolve this errors, that may have security issues embedded in them.<br><br></td></tr></tbody></table>

     * ![](images/image79.png)

 * ## Passing OTP and getting user token

     * ![](images/image324.png)

 * ## \[code\] otp verification logic

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>1) Check the expiration time:<br>#payload['creation_time'] is obtained from payload<br><br>#Timelimit is obtained from settings_basic_django.TIMELIMIT_OTP<br><br>timelimit = datetime.timedelta(seconds=settings_basic_django.TIMELIMIT_OTP)<br><br>#We check the current_time w.r.t creation_time + timelimit based on which we decide time OTP time expired or not<br><br>#Then add the error in the form and return the form<br>form.add_error(None,"OTP expired, Click on resend OTP")<br><br>2) Check the OTP<br>If creation time is within the expiration time:<br><br>#Then get payload[‘nonce’] <br><br>#Calculate secret<br><br>pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br><br>Check the pin with form_data[‘pin]<br></td></tr></tbody></table>

 * ## \[image\] otp verification logic

     * ![](images/image58.png)![](images/image288.png)![](images/image212.png)![](images/image279.png)

 * ## Code for the user\_login\_via\_otp\_form\_otp view:

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/api/views.py

     * ![](images/image346.png)![](images/image61.png)![](images/image152.png)![](images/image80.png)![](images/image318.png)![](images/image36.png)![](images/image213.png)![](images/image22.png)![](images/image73.png)![](images/image211.png)![](images/image278.png)![](images/image174.png)![](images/image70.png)![](images/image33.png)![](images/image115.png)![](images/image32.png)![](images/image304.png)![](images/image26.png)![](images/image137.png)![](images/image167.png)![](images/image291.png)![](images/image273.png)![](images/image46.png)![](images/image18.png)![](images/image130.png)![](images/image37.png)![](images/image98.png)![](images/image216.png)![](images/image1.png)![](images/image241.png)![](images/image243.png)![](images/image28.png)

 * ## \[code -- user\_login\_via\_otp\_form\_otp\]

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># ???<br>@csrf_exempt<br>def user_login_via_otp_form_otp(request):<br># ???<br><br>    # ??? Store all messages to be passed to the redirect url<br>    messages_redirect=[]<br>    # ???<br><br>    # ??? Store all the response data to be sent<br>    response_data = {}<br>    # ???<br><br>    # FORM<br>    # ???<br>    if request.method == 'POST':<br>    # ???<br><br>        import traceback<br>        #Eg: request.body<br>        # {<br>        #     "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpbWhhcnVwYS5ybnNAZ21haWwuY29tIiwibm9uY2UiOiJfVTluNXUwanYtNzJ6UjQzUTA1eEVTXzlmdEZBaWh1NlJiR1pFZ2E4VXUwIiwiY3JlYXRpb25fdGltZSI6IjIwMjAtMDMtMjBUMTI6NTc6MTcuNTUxNDc5KzAwOjAwIn0._lSMQwjAUtdvQfnwmQdNaM03mI3uYmZGZyGX_CXsK-M",<br>        #     "OTP":"943578"<br>        # }<br>        # ???<br>        try:<br>            # get form data from request.body<br>            form_data = json.loads(request.body)<br>            # ???<br>        except Exception as e:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "json.loads(request.body): "+str(e)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br><br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? CHECKING whether data has jwt_token variable exists or not<br>        if 'jwt_token' in form_data:<br>            jwt_token = form_data['jwt_token']<br>        # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? CHECKING jwt token and getting the payload<br>        try:<br>            # options = {<br>            #     'verify_exp': True,<br>            # }<br>            payload = jwt.decode(<br>                jwt_token,<br>                settings.SECRET_KEY,<br>                True,<br>                #options=options,<br>            )<br>            # ???<br>            #logger_custom_string.debug(settings.pp_dict(payload))<br>        except Exception as e:  # NoQA<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not valid"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? checking if OTP exits in form Data<br>        if 'OTP' in form_data:<br>            OTP = form_data['OTP']<br>            # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "OTP param is not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? Supplying the form data into the form<br>        form = UserLoginViaOtpFormOTP({"otp_loginconfirm":OTP})<br>        # ???<br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? checking if form is valid<br>        if form.is_valid():<br>            # ??? getting the cleaned data<br>            otp_loginconfirm = form.cleaned_data.get('otp_loginconfirm')<br>            # ???<br><br>            # ??? COMPARE TIME LIMIT FOR OTP (We check this using the time limit of jwt_token)<br>            #convert payload creation time to datetime<br>            creation_time = datetime.datetime.fromisoformat(payload['creation_time'])<br>            #datetime.timedelta(minutes=1, seconds=1)<br>            timelimit = datetime.timedelta(seconds=settings_basic_django.TIMELIMIT_OTP)<br>            current_time = datetime.datetime.now(tz=pytz.timezone('UTC'))<br>            timecheck = current_time - creation_time &lt; timelimit<br>            timedelta = current_time - creation_time<br><br>            if current_time - creation_time &gt; timelimit:<br>                form.add_error(None,"OTP expired, Click on resend OTP")<br>                remote_form = RemoteForm(form)<br>                remote_form_dict = remote_form.as_dict()<br>                # Errors in response_data['non_field_errors'] and response_data['errors']<br>                response_data.update({'form': remote_form_dict})<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': False})<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                response = HttpResponse(<br>                    response_data_json_dumps,<br>                    content_type="application/json"<br>                )<br>                # Process response for CSRF<br>                csrf_middleware.process_response(request, response)<br>                return response<br>            # ???<br><br>            # ??? Generate TOTP based on the nonce<br>            ### trying to generate a TOTP (time based One time password)<br>            # we create a nonce (number used once)<br>            # There three ways to create nonce<br>            #1) secrets.token_urlsafe() (we use this)<br>            #2) uuid.uuid4()<br>            #3) str(int(time.time()*1000))<br><br>            nonce = payload['nonce']<br><br>            # we use pyotp to generate OTP based on current system time<br>            # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>            # followed by 2–7. 0 and 1 are skipped due to their similarity<br>            # with the letters O and I<br>            # we store the common secret in .env file<br>            base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            django_secret = settings_basic_django.SECRET_KEY<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # Now convert the nonce to base32<br>            # nonce.encode("UTF-8") - converts to bytes<br>            # base64.b32encode() gives byte string<br>            # .decode('utf-8') converts the byte string to string<br>            nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br><br>            django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br><br>            # the final secret we will use in pyotp is combination of<br>            # nonce_base32 + django_secret_base32 + base32_secret<br>            pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>            pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>            pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br>            # ???<br><br>            # ??? Check the pin is valid<br>            if pin == form_data['OTP']:<br>            # ???<br><br>                # ???<br>                try:<br>                # ???<br><br>                    # ??? check for existing user and save<br>                    match = User.objects.get(email=payload['email'])<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    match.last_login2=time_now<br>                    match.recentdate_login_via_otp=time_now<br>                    match.save()<br>                    # ???<br>                    user_jwt_secret_main = match.jwt_secret<br><br>                    # ??? check match is active<br>                    if match.is_active:<br>                    # ???<br>                        #login(request,match,backend='django.contrib.auth.backends.ModelBackend')<br>                        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    else:<br>                        messages_redirect.append(email + ' is not active')<br>                        response_data.update({'messages_redirect': messages_redirect})<br>                        response_data.update({'redirect': True})<br>                        response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_email')})<br>                        response_data.update(jwt_token)<br>                        response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                        return HttpResponse(<br>                              response_data_json_dumps,<br>                              status=200,<br>                              content_type="application/json"<br>                            )<br><br>                    #Get ip address<br>                    ip = settings.get_client_ip(request)<br><br>                    # get the action type<br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # Save in the session<br>                    match_UserSessionLog = UserSessionLog(<br>                        user_email=match.email,<br>                        ip_address = ip,<br>                        user = match,<br>                        otp_used_for_otplogin=form_data['OTP'],<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        # here we <br>                        created_time=time_now<br>                    )<br>                    match_UserSessionLog.save()<br>                    usersession_created_time = match_UserSessionLog.created_time<br>                    unique_id = match_UserSessionLog.unique_id<br>                    user_jwt_secret_session = match_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    # ???<br><br>                # ???<br>                except User.DoesNotExist:<br>                # ???<br>                    """<br>                        total length of Model_meta.get_fields(include_hidden=True):  32<br>                        [<br>                            "&lt;ManyToOneRel: admin.logentry&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_groups&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_user_permissions&gt;",<br>                            "&lt;ManyToOneRel: custom_user.usersessionlog&gt;",<br>                            [<br>                                "&lt;django.db.models.fields.AutoField: id&gt;",<br>                                "STR: custom_user.User.id"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login&gt;",<br>                                "STR: custom_user.User.last_login"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_superuser&gt;",<br>                                "STR: custom_user.User.is_superuser"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_staff&gt;",<br>                                "STR: custom_user.User.is_staff"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_joined&gt;",<br>                                "STR: custom_user.User.date_joined"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: password&gt;",<br>                                "STR: custom_user.User.password"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_passwd&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_passwd"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_otp&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_otp"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_password_change&gt;",<br>                                "STR: custom_user.User.recentdate_password_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_name&gt;",<br>                                "STR: custom_user.User.first_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: last_name&gt;",<br>                                "STR: custom_user.User.last_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.EmailField: email&gt;",<br>                                "STR: custom_user.User.email"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_active&gt;",<br>                                "STR: custom_user.User.is_active"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.date_of_recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.date_of_otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.date_of_first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.TextField: about&gt;",<br>                                "STR: custom_user.User.about"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: location&gt;",<br>                                "STR: custom_user.User.location"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateField: birth_date&gt;",<br>                                "STR: custom_user.User.birth_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: modified_date&gt;",<br>                                "STR: custom_user.User.modified_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: creation_date&gt;",<br>                                "STR: custom_user.User.creation_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login2&gt;",<br>                                "STR: custom_user.User.last_login2"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.UUIDField: jwt_secret&gt;",<br>                                "STR: custom_user.User.jwt_secret"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: groups&gt;",<br>                                "STR: custom_user.User.groups"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;",<br>                                "STR: custom_user.User.user_permissions"<br>                            ]<br>                        ]<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 228, in &lt;module&gt;<br>                            print(settings.pp_odir(Model_meta.get_fields(include_hidden=True),traceback.format_stack(limit=5)))<br><br><br><br>                        Lenght of c_dict[000_null_true***********************************************************************]  9<br>                        Lenght of c_dict[001_remaining***********************************************************************]  1<br>                        Lenght of c_dict[002_null_false_and_empty_strings****************************************************]  10<br>                        Lenght of c_dict[003_auto_now_add__OR__auto_now******************************************************]  2<br>                        Lenght of c_dict[004_auto_created********************************************************************]  5<br>                        Lenght of c_dict[005_default_not_empty_string********************************************************]  5<br>                        Total lenght of c_dict:  32<br>                        {<br>                            "000_null_true***********************************************************************": {<br>                                "birth_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "date_of_first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "last_login": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "last_login2": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_otp": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_passwd": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_password_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                }<br>                            },<br>                            "001_remaining***********************************************************************": {<br>                            @@@@"jwt_secret": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.UUIDField'&gt;",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false,<br>                                    "editable": false,<br>                                    "max_length": 32<br>                                }<br>                            },<br>                            "002_null_false_and_empty_strings****************************************************": {<br>                                "about": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.TextField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 500<br>                                },<br>                            @@@@"email": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.EmailField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 254,<br>                                    "unique": true<br>                                },<br>                                "first_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                            @@@@"first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "groups": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                },<br>                                "last_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 150<br>                                },<br>                                "location": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                                "otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "user_permissions": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                }<br>                            },<br>                            "003_auto_now_add__OR__auto_now******************************************************": {<br>                                "creation_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "003_auto_now_add": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                },<br>                                "modified_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "004_auto_now": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                }<br>                            },<br>                            "004_auto_created********************************************************************": {<br>                                "User_groups+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_groups.user"<br>                                    ]<br>                                },<br>                                "User_user_permissions+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_user_permissions.user"<br>                                    ]<br>                                },<br>                                "id": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.AutoField'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "primary_key": true,<br>                                    "unique": true<br>                                },<br>                                "logentry": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: admin.LogEntry.user"<br>                                    ]<br>                                },<br>                                "usersessionlog": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.UserSessionLog.user"<br>                                    ]<br>                                }<br>                            },<br>                            "005_default_not_empty_string********************************************************": {<br>                                "date_joined": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "001_default": [<br>                                        "datetime.datetime(2020, 3, 14, 16, 27, 44, 363244, tzinfo=&lt;UTC&gt;)",<br>                                        "STR: 2020-03-14 16:27:44.363244+00:00"<br>                                    ],<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                            @@@@"is_active": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_staff": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_superuser": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "password": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "pbkdf2_sha256$180000$YoBw24luwZAV$0ZL6l6/5DgeRJv7FEGMswDP4kGM+tE04rSfA3FDqYbQ=",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 128<br>                                }<br>                            }<br>                        }<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 248, in &lt;module&gt;<br>                            print(settings.pp_odir(c_dict,traceback.format_stack(limit=5)))<br><br>                    """<br>                    # ??? Create a new user<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    newuser = User(<br>                        email=payload['email'],<br>                        first_otp_used_for_otplogin=pin,<br>                        date_of_first_otp_used_for_otplogin=time_now,<br>                        last_login2=time_now,<br>                        recentdate_login_via_otp=time_now,<br>                        is_active=True<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        #date_joined=time_now<br>                        )<br>                    newuser.save()<br>                    # ???<br><br>                    user_jwt_secret_main = newuser.jwt_secret<br><br>                    # Get the client ip:<br>                    ip = settings.get_client_ip(request)<br><br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # ??? Save in the session<br>                    new_UserSessionLog = UserSessionLog(<br>                        user_email=newuser.email,<br>                        ip_address = ip,<br>                        user = newuser,<br>                        otp_used_for_otplogin=pin,<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        created_time=time_now,<br>                    )<br><br>                    new_UserSessionLog.save()<br>                    # ???<br>                    unique_id = new_UserSessionLog.unique_id<br>                    user_jwt_secret_session = new_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    usersession_created_time = new_UserSessionLog.created_time<br><br>                # ??? Create a message to show that OTP is sent to email<br>                messages_redirect.append('Login Successful')<br>                # ???<br><br>                # ??? Create token authenticating a user<br>                django_secret = settings_basic_django.SECRET_KEY<br><br>                # we also use the secret form Userssion and User tables<br>                user_toke_secret = django_secret + user_jwt_secret_main.hex + user_jwt_secret_session.hex<br>                payload_token = {<br>                    'email': payload['email'],<br>                    'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>                }<br>                user_token = {<br>                    'token':jwt.encode(payload_token, user_toke_secret, algorithm='HS256').decode('utf-8'),<br>                    'unique_id':unique_id<br>                }<br>                # ???<br><br>                # ??? Add all the data to be sent to the response_data object<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': True})<br>                response_data.update({'redirect_url': reverse('articles_namespace:articles')})<br>                response_data.update({"user_token":user_token})<br>                # ???<br><br>                # ??? Create json string<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                # ???<br><br>                # ??? send the json_string of jwt_token<br>                return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br>                # ???<br><br>            # ??? if form is not valid<br>            form.add_error(None,"Form Error: Wrong OTP entered")<br>            remote_form = RemoteForm(form)<br>            remote_form_dict = remote_form.as_dict()<br>            # Errors in response_data['non_field_errors'] and response_data['errors']<br>            response_data.update({'form': remote_form_dict})<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': False})<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            response = HttpResponse(<br>                response_data_json_dumps,<br>                content_type="application/json"<br>            )<br>            # Process response for CSRF<br>            csrf_middleware.process_response(request, response)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return response<br>            # ???<br>    else:<br>        #logger_custom_string.debug(request.GET.get('resendotp'))<br>        #logger_custom_string.debug(settings.pp_dict(request.GET))<br>        #logger_custom_string.debug('resendotp' in request.GET)<br><br>        if 'resendotp' in request.GET:<br><br>            import traceback<br>            form_data = json.loads(request.body)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # CHECKING whether the session variable exists or not<br>            if 'jwt_token' in form_data:<br>                jwt_token = form_data['jwt_token']<br>            else:<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not found"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            # CHECKING jwt token and getting the payload<br>            try:<br>                # options = {<br>                #     'verify_exp': True,<br>                # }<br>                payload = jwt.decode(<br>                    jwt_token,<br>                    settings.SECRET_KEY,<br>                    True,<br>                    #options=options,<br>                )<br>                #logger_custom_string.debug(settings.pp_dict(payload))<br>            except Exception as e:  # NoQA<br>                #logger_custom_string.debug(str(e))<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not valid"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            email = payload['email']<br><br>            pin, nonce = generate_pin_pyopt()<br>            # generate a random pin using crpto functions<br>            #pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            send_email_task.delay(email,subject,message)<br><br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br><br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            logger_custom_string.debug(settings_basic_django.pp_odir(getattr(request, '_messages', []),traceback.format_stack(limit=5)))<br><br>            messages_redirect.append('OTP send to email: ' + email)<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': True})<br>            response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_otp')})<br>            response_data.update(jwt_token)<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br><br>        form = UserLoginViaOtpFormOTP()<br><br>    remote_form = RemoteForm(form)<br>    remote_form_dict = remote_form.as_dict()<br>    # Errors in response_data['non_field_errors'] and response_data['errors']<br>    response_data.update({'form': remote_form_dict})<br>    response_data.update({'messages_redirect': messages_redirect})<br>    response_data.update({'redirect': False})<br><br><br>    response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br><br><br><br>    response = HttpResponse(<br>        response_data_json_dumps,<br>        content_type="application/json"<br>    )<br>    import traceback<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    return response<br><br></td></tr></tbody></table>

     * \[code\] FULL basic\_django/login\_register\_password/api/views.py 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import jwt<br>import json<br>from django.shortcuts import render, redirect, reverse<br>from django.http import HttpResponse<br>from basic_django import settings<br>from custom_user.models import User, UserSessionLog, ActionTypeForUserSessionLog<br>from login_register_password.forms import UserLoginViaOtpFormEmail, UserLoginViaOtpFormOTP<br>from django.contrib import messages<br>from basic_django.tasks import send_email_task<br>from django.views.decorators.csrf import csrf_exempt<br>from django.middleware.csrf import CsrfViewMiddleware<br>import secrets<br>import base64<br>import pyotp<br>from django_remote_forms.forms import RemoteForm<br>from django.core.serializers.json import DjangoJSONEncoder<br>import re<br>from django.template.loader import render_to_string<br>import datetime<br>import pytz<br>from django.utils.timezone import make_aware<br>from django.utils import timezone<br>from rest_framework import exceptions<br><br><br>###    ## LOGGING<br>import logging<br>import traceback<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings as settings_basic_django<br>#usage1: To show anything as string<br>#logger_custom_string.debug(settings_basic_django.anything("Hare Krishna",traceback.format_stack(limit=5)))<br>#usage2: to show dict or obj<br>#logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>#logger_custom_string.debug(settings_basic_django.pp_odir(obj,traceback.format_stack(limit=5)))  # This will pretty print all the properties from dir(obj)<br><br><br># the following function will generate a pin using pyOTP and also a nonce<br>def generate_pin_pyopt():<br>    ### trying to generate a TOTP (time based One time password)<br>    # we create a nonce (number used once)<br>    # There three ways to create nonce<br>    #1) secrets.token_urlsafe() (we use this)<br>    #2) uuid.uuid4()<br>    #3) str(int(time.time()*1000))<br><br>    nonce = secrets.token_urlsafe()<br><br>    # we use pyotp to generate OTP based on current system time<br>    # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>    # followed by 2–7. 0 and 1 are skipped due to their similarity<br>    # with the letters O and I<br>    # we store the common secret in .env file<br>    base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    django_secret = settings_basic_django.SECRET_KEY<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # Now convert the nonce to base32<br>    # nonce.encode("UTF-8") - converts to bytes<br>    # base64.b32encode() gives byte string<br>    # .decode('utf-8') converts the byte string to string<br>    nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # the final secret we will use in pyotp is combination of<br>    # nonce_base32 + django_secret_base32 + base32_secret<br>    pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>    pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    return pin, nonce<br><br><br><br><br><br># ???<br>@csrf_exempt<br>def user_login_via_otp_form_email(request):<br># ???<br><br>    # messages_redirect are the those messages which we want to show after redirect<br>    # the client has to store them and pass on to the redirect url output<br>    # ??? Store all messages to be passed to the redirect url<br>    messages_redirect=[]<br>    # ???<br><br>    csrf_middleware = CsrfViewMiddleware()<br><br>    # response_data: is the python object which will be converted to json string and passed to httpresponse<br>    # ??? Store all the response data to be sent<br>    response_data = {}<br>    # ???<br><br>    import traceback<br>    logger_custom_string.debug(settings_basic_django.anything(request.method,traceback.format_stack(limit=5)))<br><br>    # ???<br>    if request.method == 'GET':<br>    # ???<br>        # Get form definition<br>        #form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>        # ??? get the form<br>        form = UserLoginViaOtpFormEmail()<br>        # ???<br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # ???<br>    elif request.method == 'POST':<br>    # ???<br>        # if request.content_type  != 'application/json':<br>        #     return HttpResponse(json.dumps({"detail": "Unsupported media type \"'%s'\" in request." % request.content_type}), content_type="application/json",status=401);<br>        # # Process request for CSRF<br>        csrf_middleware.process_view(request, None, None, None)<br>        logger_custom_string.debug(settings_basic_django.anything(request.body,traceback.format_stack(limit=5)))<br><br>        # Check for request.body is proper json string.<br>        # ???<br>        try:<br>            # get form data from request.body<br>            form_data = json.loads(request.body)<br>            # ???<br>        except Exception as e:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "json.loads(request.body): "+str(e)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        logger_custom_string.debug(settings_basic_django.pp_odir(form_data,traceback.format_stack(limit=5)))<br>        # ??? pass the form_data to form<br>        form = UserLoginViaOtpFormEmail(form_data)<br><br>        if form.is_valid():<br>        # ???<br><br>            # ??? Get the email<br>            email = form.cleaned_data.get('email')<br>            # ???<br><br>            # ??? Generate pin and nonce<br>            pin, nonce = generate_pin_pyopt()<br>            # ???<br>            # generate a random pin using crpto functions<br>            #pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            # ??? Email the pin<br>            send_email_task.delay(email,subject,message)<br>            # ???<br><br>            # ??? Create jwt_token with email, nonce and creation_time<br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br>            # ???<br><br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            logger_custom_string.debug(settings_basic_django.pp_odir(getattr(request, '_messages', []),traceback.format_stack(limit=5)))<br><br>            # ??? Create a message to show that OTP is sent to email<br>            messages_redirect.append('OTP send to email: ' + email)<br>            # ???<br><br>            # ??? Add all the data to be sent to the response_data object<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': True})<br>            response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_otp')})<br>            response_data.update(jwt_token)<br>            # ???<br><br>            # ??? Create json string<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            # ???<br><br>            # ??? send the json_string of jwt_token<br>            return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br>            # ???<br><br>    # ??? convert the form to dict<br>    remote_form = RemoteForm(form)<br>    remote_form_dict = remote_form.as_dict()<br>    # ???<br>    <br>    # ??? Add all the data to be sent to the response_data object<br>    response_data.update({'form': remote_form_dict})<br>    response_data.update({'messages_redirect': messages_redirect})<br>    response_data.update({'redirect': False})<br>    # ???<br><br>    # ??? create json string<br>    response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>    # ???<br><br><br><br>    # ??? Send the form as json string<br>    response = HttpResponse(<br>        response_data_json_dumps,<br>        content_type="application/json"<br>    )<br>    # ???<br><br>    # Process response for CSRF<br>    csrf_middleware.process_response(request, response)<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    # ???<br>    return response<br>    # ???<br><br># ???<br>@csrf_exempt<br>def user_login_via_otp_form_otp(request):<br># ???<br><br>    # ??? Store all messages to be passed to the redirect url<br>    messages_redirect=[]<br>    # ???<br><br>    # ??? Store all the response data to be sent<br>    response_data = {}<br>    # ???<br><br>    # FORM<br>    # ???<br>    if request.method == 'POST':<br>    # ???<br><br>        import traceback<br>        #Eg: request.body<br>        # {<br>        #     "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpbWhhcnVwYS5ybnNAZ21haWwuY29tIiwibm9uY2UiOiJfVTluNXUwanYtNzJ6UjQzUTA1eEVTXzlmdEZBaWh1NlJiR1pFZ2E4VXUwIiwiY3JlYXRpb25fdGltZSI6IjIwMjAtMDMtMjBUMTI6NTc6MTcuNTUxNDc5KzAwOjAwIn0._lSMQwjAUtdvQfnwmQdNaM03mI3uYmZGZyGX_CXsK-M",<br>        #     "OTP":"943578"<br>        # }<br>        # ???<br>        try:<br>            # get form data from request.body<br>            form_data = json.loads(request.body)<br>            # ???<br>        except Exception as e:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "json.loads(request.body): "+str(e)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br><br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? CHECKING whether data has jwt_token variable exists or not<br>        if 'jwt_token' in form_data:<br>            jwt_token = form_data['jwt_token']<br>        # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? CHECKING jwt token and getting the payload<br>        try:<br>            # options = {<br>            #     'verify_exp': True,<br>            # }<br>            payload = jwt.decode(<br>                jwt_token,<br>                settings.SECRET_KEY,<br>                True,<br>                #options=options,<br>            )<br>            # ???<br>            #logger_custom_string.debug(settings.pp_dict(payload))<br>        except Exception as e:  # NoQA<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not valid"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? checking if OTP exits in form Data<br>        if 'OTP' in form_data:<br>            OTP = form_data['OTP']<br>            # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "OTP param is not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? Supplying the form data into the form<br>        form = UserLoginViaOtpFormOTP({"otp_loginconfirm":OTP})<br>        # ???<br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? checking if form is valid<br>        if form.is_valid():<br>            # ??? getting the cleaned data<br>            otp_loginconfirm = form.cleaned_data.get('otp_loginconfirm')<br>            # ???<br><br>            # ??? COMPARE TIME LIMIT FOR OTP (We check this using the time limit of jwt_token)<br>            #convert payload creation time to datetime<br>            creation_time = datetime.datetime.fromisoformat(payload['creation_time'])<br>            #datetime.timedelta(minutes=1, seconds=1)<br>            timelimit = datetime.timedelta(seconds=settings_basic_django.TIMELIMIT_OTP)<br>            current_time = datetime.datetime.now(tz=pytz.timezone('UTC'))<br>            timecheck = current_time - creation_time &lt; timelimit<br>            timedelta = current_time - creation_time<br><br>            if current_time - creation_time &gt; timelimit:<br>                form.add_error(None,"OTP expired, Click on resend OTP")<br>                remote_form = RemoteForm(form)<br>                remote_form_dict = remote_form.as_dict()<br>                # Errors in response_data['non_field_errors'] and response_data['errors']<br>                response_data.update({'form': remote_form_dict})<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': False})<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                response = HttpResponse(<br>                    response_data_json_dumps,<br>                    content_type="application/json"<br>                )<br>                # Process response for CSRF<br>                csrf_middleware.process_response(request, response)<br>                return response<br>            # ???<br><br>            # ??? Generate TOTP based on the nonce<br>            ### trying to generate a TOTP (time based One time password)<br>            # we create a nonce (number used once)<br>            # There three ways to create nonce<br>            #1) secrets.token_urlsafe() (we use this)<br>            #2) uuid.uuid4()<br>            #3) str(int(time.time()*1000))<br><br>            nonce = payload['nonce']<br><br>            # we use pyotp to generate OTP based on current system time<br>            # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>            # followed by 2–7. 0 and 1 are skipped due to their similarity<br>            # with the letters O and I<br>            # we store the common secret in .env file<br>            base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            django_secret = settings_basic_django.SECRET_KEY<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # Now convert the nonce to base32<br>            # nonce.encode("UTF-8") - converts to bytes<br>            # base64.b32encode() gives byte string<br>            # .decode('utf-8') converts the byte string to string<br>            nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br><br>            django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br><br>            # the final secret we will use in pyotp is combination of<br>            # nonce_base32 + django_secret_base32 + base32_secret<br>            pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>            pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>            pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br>            # ???<br><br>            # ??? Check the pin is valid<br>            if pin == form_data['OTP']:<br>            # ???<br><br>                # ???<br>                try:<br>                # ???<br><br>                    # ??? check for existing user and save<br>                    match = User.objects.get(email=payload['email'])<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    match.last_login2=time_now<br>                    match.recentdate_login_via_otp=time_now<br>                    match.save()<br>                    # ???<br>                    user_jwt_secret_main = match.jwt_secret<br><br>                    # ??? check match is active<br>                    if match.is_active:<br>                    # ???<br>                        #login(request,match,backend='django.contrib.auth.backends.ModelBackend')<br>                        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    else:<br>                        messages_redirect.append(email + ' is not active')<br>                        response_data.update({'messages_redirect': messages_redirect})<br>                        response_data.update({'redirect': True})<br>                        response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_email')})<br>                        response_data.update(jwt_token)<br>                        response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                        return HttpResponse(<br>                              response_data_json_dumps,<br>                              status=200,<br>                              content_type="application/json"<br>                            )<br><br>                    #Get ip address<br>                    ip = settings.get_client_ip(request)<br><br>                    # get the action type<br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # Save in the session<br>                    match_UserSessionLog = UserSessionLog(<br>                        user_email=match.email,<br>                        ip_address = ip,<br>                        user = match,<br>                        otp_used_for_otplogin=form_data['OTP'],<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        # here we <br>                        created_time=time_now<br>                    )<br>                    match_UserSessionLog.save()<br>                    usersession_created_time = match_UserSessionLog.created_time<br>                    unique_id = match_UserSessionLog.unique_id<br>                    user_jwt_secret_session = match_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    # ???<br><br>                # ???<br>                except User.DoesNotExist:<br>                # ???<br>                    """<br>                        total length of Model_meta.get_fields(include_hidden=True):  32<br>                        [<br>                            "&lt;ManyToOneRel: admin.logentry&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_groups&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_user_permissions&gt;",<br>                            "&lt;ManyToOneRel: custom_user.usersessionlog&gt;",<br>                            [<br>                                "&lt;django.db.models.fields.AutoField: id&gt;",<br>                                "STR: custom_user.User.id"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login&gt;",<br>                                "STR: custom_user.User.last_login"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_superuser&gt;",<br>                                "STR: custom_user.User.is_superuser"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_staff&gt;",<br>                                "STR: custom_user.User.is_staff"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_joined&gt;",<br>                                "STR: custom_user.User.date_joined"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: password&gt;",<br>                                "STR: custom_user.User.password"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_passwd&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_passwd"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_otp&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_otp"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_password_change&gt;",<br>                                "STR: custom_user.User.recentdate_password_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_name&gt;",<br>                                "STR: custom_user.User.first_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: last_name&gt;",<br>                                "STR: custom_user.User.last_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.EmailField: email&gt;",<br>                                "STR: custom_user.User.email"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_active&gt;",<br>                                "STR: custom_user.User.is_active"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.date_of_recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.date_of_otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.date_of_first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.TextField: about&gt;",<br>                                "STR: custom_user.User.about"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: location&gt;",<br>                                "STR: custom_user.User.location"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateField: birth_date&gt;",<br>                                "STR: custom_user.User.birth_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: modified_date&gt;",<br>                                "STR: custom_user.User.modified_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: creation_date&gt;",<br>                                "STR: custom_user.User.creation_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login2&gt;",<br>                                "STR: custom_user.User.last_login2"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.UUIDField: jwt_secret&gt;",<br>                                "STR: custom_user.User.jwt_secret"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: groups&gt;",<br>                                "STR: custom_user.User.groups"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;",<br>                                "STR: custom_user.User.user_permissions"<br>                            ]<br>                        ]<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 228, in &lt;module&gt;<br>                            print(settings.pp_odir(Model_meta.get_fields(include_hidden=True),traceback.format_stack(limit=5)))<br><br><br><br>                        Lenght of c_dict[000_null_true***********************************************************************]  9<br>                        Lenght of c_dict[001_remaining***********************************************************************]  1<br>                        Lenght of c_dict[002_null_false_and_empty_strings****************************************************]  10<br>                        Lenght of c_dict[003_auto_now_add__OR__auto_now******************************************************]  2<br>                        Lenght of c_dict[004_auto_created********************************************************************]  5<br>                        Lenght of c_dict[005_default_not_empty_string********************************************************]  5<br>                        Total lenght of c_dict:  32<br>                        {<br>                            "000_null_true***********************************************************************": {<br>                                "birth_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "date_of_first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "last_login": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "last_login2": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_otp": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_passwd": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_password_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                }<br>                            },<br>                            "001_remaining***********************************************************************": {<br>                            @@@@"jwt_secret": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.UUIDField'&gt;",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false,<br>                                    "editable": false,<br>                                    "max_length": 32<br>                                }<br>                            },<br>                            "002_null_false_and_empty_strings****************************************************": {<br>                                "about": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.TextField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 500<br>                                },<br>                            @@@@"email": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.EmailField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 254,<br>                                    "unique": true<br>                                },<br>                                "first_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                            @@@@"first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "groups": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                },<br>                                "last_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 150<br>                                },<br>                                "location": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                                "otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "user_permissions": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                }<br>                            },<br>                            "003_auto_now_add__OR__auto_now******************************************************": {<br>                                "creation_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "003_auto_now_add": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                },<br>                                "modified_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "004_auto_now": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                }<br>                            },<br>                            "004_auto_created********************************************************************": {<br>                                "User_groups+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_groups.user"<br>                                    ]<br>                                },<br>                                "User_user_permissions+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_user_permissions.user"<br>                                    ]<br>                                },<br>                                "id": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.AutoField'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "primary_key": true,<br>                                    "unique": true<br>                                },<br>                                "logentry": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: admin.LogEntry.user"<br>                                    ]<br>                                },<br>                                "usersessionlog": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.UserSessionLog.user"<br>                                    ]<br>                                }<br>                            },<br>                            "005_default_not_empty_string********************************************************": {<br>                                "date_joined": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "001_default": [<br>                                        "datetime.datetime(2020, 3, 14, 16, 27, 44, 363244, tzinfo=&lt;UTC&gt;)",<br>                                        "STR: 2020-03-14 16:27:44.363244+00:00"<br>                                    ],<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                            @@@@"is_active": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_staff": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_superuser": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "password": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "pbkdf2_sha256$180000$YoBw24luwZAV$0ZL6l6/5DgeRJv7FEGMswDP4kGM+tE04rSfA3FDqYbQ=",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 128<br>                                }<br>                            }<br>                        }<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 248, in &lt;module&gt;<br>                            print(settings.pp_odir(c_dict,traceback.format_stack(limit=5)))<br><br>                    """<br>                    # ??? Create a new user<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    newuser = User(<br>                        email=payload['email'],<br>                        first_otp_used_for_otplogin=pin,<br>                        date_of_first_otp_used_for_otplogin=time_now,<br>                        last_login2=time_now,<br>                        recentdate_login_via_otp=time_now,<br>                        is_active=True<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        #date_joined=time_now<br>                        )<br>                    newuser.save()<br>                    # ???<br><br>                    user_jwt_secret_main = newuser.jwt_secret<br><br>                    # Get the client ip:<br>                    ip = settings.get_client_ip(request)<br><br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # ??? Save in the session<br>                    new_UserSessionLog = UserSessionLog(<br>                        user_email=newuser.email,<br>                        ip_address = ip,<br>                        user = newuser,<br>                        otp_used_for_otplogin=pin,<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        created_time=time_now,<br>                    )<br><br>                    new_UserSessionLog.save()<br>                    # ???<br>                    unique_id = new_UserSessionLog.unique_id<br>                    user_jwt_secret_session = new_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    usersession_created_time = new_UserSessionLog.created_time<br><br>                # ??? Create a message to show that OTP is sent to email<br>                messages_redirect.append('Login Successful')<br>                # ???<br><br>                # ??? Create token authenticating a user<br>                django_secret = settings_basic_django.SECRET_KEY<br><br>                # we also use the secret form Userssion and User tables<br>                user_toke_secret = django_secret + user_jwt_secret_main.hex + user_jwt_secret_session.hex<br>                payload_token = {<br>                    'email': payload['email'],<br>                    'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>                }<br>                user_token = {<br>                    'token':jwt.encode(payload_token, user_toke_secret, algorithm='HS256').decode('utf-8'),<br>                    'unique_id':unique_id<br>                }<br>                # ???<br><br>                # ??? Add all the data to be sent to the response_data object<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': True})<br>                response_data.update({'redirect_url': reverse('articles_namespace:articles')})<br>                response_data.update({"user_token":user_token})<br>                # ???<br><br>                # ??? Create json string<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                # ???<br><br>                # ??? send the json_string of jwt_token<br>                return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br>                # ???<br><br>            # ??? if form is not valid<br>            form.add_error(None,"Form Error: Wrong OTP entered")<br>            remote_form = RemoteForm(form)<br>            remote_form_dict = remote_form.as_dict()<br>            # Errors in response_data['non_field_errors'] and response_data['errors']<br>            response_data.update({'form': remote_form_dict})<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': False})<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            response = HttpResponse(<br>                response_data_json_dumps,<br>                content_type="application/json"<br>            )<br>            # Process response for CSRF<br>            csrf_middleware.process_response(request, response)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return response<br>            # ???<br>    else:<br>        #logger_custom_string.debug(request.GET.get('resendotp'))<br>        #logger_custom_string.debug(settings.pp_dict(request.GET))<br>        #logger_custom_string.debug('resendotp' in request.GET)<br><br>        if 'resendotp' in request.GET:<br><br>            import traceback<br>            form_data = json.loads(request.body)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # CHECKING whether the session variable exists or not<br>            if 'jwt_token' in form_data:<br>                jwt_token = form_data['jwt_token']<br>            else:<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not found"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            # CHECKING jwt token and getting the payload<br>            try:<br>                # options = {<br>                #     'verify_exp': True,<br>                # }<br>                payload = jwt.decode(<br>                    jwt_token,<br>                    settings.SECRET_KEY,<br>                    True,<br>                    #options=options,<br>                )<br>                #logger_custom_string.debug(settings.pp_dict(payload))<br>            except Exception as e:  # NoQA<br>                #logger_custom_string.debug(str(e))<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not valid"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            email = payload['email']<br><br>            pin, nonce = generate_pin_pyopt()<br>            # generate a random pin using crpto functions<br>            #pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            send_email_task.delay(email,subject,message)<br><br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br><br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            logger_custom_string.debug(settings_basic_django.pp_odir(getattr(request, '_messages', []),traceback.format_stack(limit=5)))<br><br>            messages_redirect.append('OTP send to email: ' + email)<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': True})<br>            response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_otp')})<br>            response_data.update(jwt_token)<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br><br>        form = UserLoginViaOtpFormOTP()<br><br>    remote_form = RemoteForm(form)<br>    remote_form_dict = remote_form.as_dict()<br>    # Errors in response_data['non_field_errors'] and response_data['errors']<br>    response_data.update({'form': remote_form_dict})<br>    response_data.update({'messages_redirect': messages_redirect})<br>    response_data.update({'redirect': False})<br><br><br>    response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br><br><br><br>    response = HttpResponse(<br>        response_data_json_dumps,<br>        content_type="application/json"<br>    )<br>    import traceback<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    return response<br><br><br>### #Basic one<br>### @csrf_exempt<br>### def user_login_via_otp_form_email(request):<br>###     response_data = {}<br>###     if request.method == 'GET':<br>###         # Get form definition<br>###         form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>###     elif request.method == 'POST':<br>###         form_data = json.loads(request.body)<br>###         logger_custom_string.debug(settings_basic_django.pp_odir(form_data,traceback.format_stack(limit=5)))<br>###         form = UserLoginViaOtpFormEmail(form_data)<br>###     html = "&lt;html&gt;&lt;body&gt;API TESTING&lt;/body&gt;&lt;/html&gt;"<br>###     return HttpResponse(html)<br></td></tr></tbody></table>

 * ## \[image\] FULL views.py file

     * ![](images/image114.png)![](images/image321.png)![](images/image282.png)![](images/image95.png)![](images/image31.png)![](images/image347.png)![](images/image105.png)![](images/image233.png)![](images/image230.png)![](images/image298.png)![](images/image329.png)![](images/image250.png)![](images/image134.png)![](images/image71.png)![](images/image53.png)![](images/image289.png)![](images/image123.png)![](images/image88.png)![](images/image328.png)![](images/image337.png)![](images/image202.png)![](images/image255.png)![](images/image45.png)![](images/image165.png)![](images/image178.png)![](images/image249.png)

 * ## \[code\] full views.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import jwt<br>import json<br>from django.shortcuts import render, redirect, reverse<br>from django.http import HttpResponse<br>from basic_django import settings<br>from custom_user.models import User, UserSessionLog, ActionTypeForUserSessionLog<br>from login_register_password.forms import UserLoginViaOtpFormEmail, UserLoginViaOtpFormOTP<br>from django.contrib import messages<br>from basic_django.tasks import send_email_task<br>from django.views.decorators.csrf import csrf_exempt<br>from django.middleware.csrf import CsrfViewMiddleware<br>import secrets<br>import base64<br>import pyotp<br>from django_remote_forms.forms import RemoteForm<br>from django.core.serializers.json import DjangoJSONEncoder<br>import re<br>from django.template.loader import render_to_string<br>import datetime<br>import pytz<br>from django.utils.timezone import make_aware<br>from django.utils import timezone<br>from rest_framework import exceptions<br><br><br>###    ## LOGGING<br>import logging<br>import traceback<br>logger_custom_string = logging.getLogger("custom_string")<br>from basic_django import settings as settings_basic_django<br>#usage1: To show anything as string<br>#logger_custom_string.debug(settings_basic_django.anything("Hare Krishna",traceback.format_stack(limit=5)))<br>#usage2: to show dict or obj<br>#logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>#logger_custom_string.debug(settings_basic_django.pp_odir(obj,traceback.format_stack(limit=5)))  # This will pretty print all the properties from dir(obj)<br><br><br># the following function will generate a pin using pyOTP and also a nonce<br>def generate_pin_pyopt():<br>    ### trying to generate a TOTP (time based One time password)<br>    # we create a nonce (number used once)<br>    # There three ways to create nonce<br>    #1) secrets.token_urlsafe() (we use this)<br>    #2) uuid.uuid4()<br>    #3) str(int(time.time()*1000))<br><br>    nonce = secrets.token_urlsafe()<br><br>    # we use pyotp to generate OTP based on current system time<br>    # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>    # followed by 2–7. 0 and 1 are skipped due to their similarity<br>    # with the letters O and I<br>    # we store the common secret in .env file<br>    base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    django_secret = settings_basic_django.SECRET_KEY<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # Now convert the nonce to base32<br>    # nonce.encode("UTF-8") - converts to bytes<br>    # base64.b32encode() gives byte string<br>    # .decode('utf-8') converts the byte string to string<br>    nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # the final secret we will use in pyotp is combination of<br>    # nonce_base32 + django_secret_base32 + base32_secret<br>    pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>    pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br><br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    return pin, nonce<br><br><br><br><br><br># ???<br>@csrf_exempt<br>def user_login_via_otp_form_email(request):<br># ???<br><br>    # messages_redirect are the those messages which we want to show after redirect<br>    # the client has to store them and pass on to the redirect url output<br>    # ??? Store all messages to be passed to the redirect url<br>    messages_redirect=[]<br>    # ???<br><br>    csrf_middleware = CsrfViewMiddleware()<br><br>    # response_data: is the python object which will be converted to json string and passed to httpresponse<br>    # ??? Store all the response data to be sent<br>    response_data = {}<br>    # ???<br><br>    import traceback<br>    logger_custom_string.debug(settings_basic_django.anything(request.method,traceback.format_stack(limit=5)))<br><br>    # ???<br>    if request.method == 'GET':<br>    # ???<br>        # Get form definition<br>        #form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>        # ??? get the form<br>        form = UserLoginViaOtpFormEmail()<br>        # ???<br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>    # ???<br>    elif request.method == 'POST':<br>    # ???<br>        # if request.content_type  != 'application/json':<br>        #     return HttpResponse(json.dumps({"detail": "Unsupported media type \"'%s'\" in request." % request.content_type}), content_type="application/json",status=401);<br>        # # Process request for CSRF<br>        csrf_middleware.process_view(request, None, None, None)<br>        logger_custom_string.debug(settings_basic_django.anything(request.body,traceback.format_stack(limit=5)))<br><br>        # Check for request.body is proper json string.<br>        # ???<br>        try:<br>            # get form data from request.body<br>            form_data = json.loads(request.body)<br>            # ???<br>        except Exception as e:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "json.loads(request.body): "+str(e)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        logger_custom_string.debug(settings_basic_django.pp_odir(form_data,traceback.format_stack(limit=5)))<br>        # ??? pass the form_data to form<br>        form = UserLoginViaOtpFormEmail(form_data)<br><br>        if form.is_valid():<br>        # ???<br><br>            # ??? Get the email<br>            email = form.cleaned_data.get('email')<br>            # ???<br><br>            # ??? Generate pin and nonce<br>            pin, nonce = generate_pin_pyopt()<br>            # ???<br>            # generate a random pin using crpto functions<br>            #pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            # ??? Email the pin<br>            send_email_task.delay(email,subject,message)<br>            # ???<br><br>            # ??? Create jwt_token with email, nonce and creation_time<br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br>            # ???<br><br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            logger_custom_string.debug(settings_basic_django.pp_odir(getattr(request, '_messages', []),traceback.format_stack(limit=5)))<br><br>            # ??? Create a message to show that OTP is sent to email<br>            messages_redirect.append('OTP send to email: ' + email)<br>            # ???<br><br>            # ??? Add all the data to be sent to the response_data object<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': True})<br>            response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_otp')})<br>            response_data.update(jwt_token)<br>            # ???<br><br>            # ??? Create json string<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            # ???<br><br>            # ??? send the json_string of jwt_token<br>            return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br>            # ???<br><br>    # ??? convert the form to dict<br>    remote_form = RemoteForm(form)<br>    remote_form_dict = remote_form.as_dict()<br>    # ???<br>    <br>    # ??? Add all the data to be sent to the response_data object<br>    response_data.update({'form': remote_form_dict})<br>    response_data.update({'messages_redirect': messages_redirect})<br>    response_data.update({'redirect': False})<br>    # ???<br><br>    # ??? create json string<br>    response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>    # ???<br><br><br><br>    # ??? Send the form as json string<br>    response = HttpResponse(<br>        response_data_json_dumps,<br>        content_type="application/json"<br>    )<br>    # ???<br><br>    # Process response for CSRF<br>    csrf_middleware.process_response(request, response)<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    # ???<br>    return response<br>    # ???<br><br># ???<br>@csrf_exempt<br>def user_login_via_otp_form_otp(request):<br># ???<br><br>    # ??? Store all messages to be passed to the redirect url<br>    messages_redirect=[]<br>    # ???<br><br>    # ??? Store all the response data to be sent<br>    response_data = {}<br>    # ???<br><br>    # FORM<br>    # ???<br>    if request.method == 'POST':<br>    # ???<br><br>        import traceback<br>        #Eg: request.body<br>        # {<br>        #     "jwt_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNpbWhhcnVwYS5ybnNAZ21haWwuY29tIiwibm9uY2UiOiJfVTluNXUwanYtNzJ6UjQzUTA1eEVTXzlmdEZBaWh1NlJiR1pFZ2E4VXUwIiwiY3JlYXRpb25fdGltZSI6IjIwMjAtMDMtMjBUMTI6NTc6MTcuNTUxNDc5KzAwOjAwIn0._lSMQwjAUtdvQfnwmQdNaM03mI3uYmZGZyGX_CXsK-M",<br>        #     "OTP":"943578"<br>        # }<br>        # ???<br>        try:<br>            # get form data from request.body<br>            form_data = json.loads(request.body)<br>            # ???<br>        except Exception as e:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "json.loads(request.body): "+str(e)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br><br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? CHECKING whether data has jwt_token variable exists or not<br>        if 'jwt_token' in form_data:<br>            jwt_token = form_data['jwt_token']<br>        # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? CHECKING jwt token and getting the payload<br>        try:<br>            # options = {<br>            #     'verify_exp': True,<br>            # }<br>            payload = jwt.decode(<br>                jwt_token,<br>                settings.SECRET_KEY,<br>                True,<br>                #options=options,<br>            )<br>            # ???<br>            #logger_custom_string.debug(settings.pp_dict(payload))<br>        except Exception as e:  # NoQA<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "jwt_token not valid"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? checking if OTP exits in form Data<br>        if 'OTP' in form_data:<br>            OTP = form_data['OTP']<br>            # ???<br>        else:<br>            status_code = 400<br>            message = "The request body is not valid."<br>            # You should log this error because this usually means your front end has a bug.<br>            # do you whant to explain anything?<br>            explanation = "OTP param is not found"<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return HttpResponse(<br>                  json.dumps({'message':message,'explanation':explanation}),<br>                  status=status_code,<br>                  content_type="application/json"<br>                )<br><br>        # ??? Supplying the form data into the form<br>        form = UserLoginViaOtpFormOTP({"otp_loginconfirm":OTP})<br>        # ???<br>        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>        # ??? checking if form is valid<br>        if form.is_valid():<br>            # ??? getting the cleaned data<br>            otp_loginconfirm = form.cleaned_data.get('otp_loginconfirm')<br>            # ???<br><br>            # ??? COMPARE TIME LIMIT FOR OTP (We check this using the time limit of jwt_token)<br>            #convert payload creation time to datetime<br>            creation_time = datetime.datetime.fromisoformat(payload['creation_time'])<br>            #datetime.timedelta(minutes=1, seconds=1)<br>            timelimit = datetime.timedelta(seconds=settings_basic_django.TIMELIMIT_OTP)<br>            current_time = datetime.datetime.now(tz=pytz.timezone('UTC'))<br>            timecheck = current_time - creation_time &lt; timelimit<br>            timedelta = current_time - creation_time<br><br>            if current_time - creation_time &gt; timelimit:<br>                form.add_error(None,"OTP expired, Click on resend OTP")<br>                remote_form = RemoteForm(form)<br>                remote_form_dict = remote_form.as_dict()<br>                # Errors in response_data['non_field_errors'] and response_data['errors']<br>                response_data.update({'form': remote_form_dict})<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': False})<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                response = HttpResponse(<br>                    response_data_json_dumps,<br>                    content_type="application/json"<br>                )<br>                return response<br>            # ???<br><br>            # ??? Generate TOTP based on the nonce<br>            ### trying to generate a TOTP (time based One time password)<br>            # we create a nonce (number used once)<br>            # There three ways to create nonce<br>            #1) secrets.token_urlsafe() (we use this)<br>            #2) uuid.uuid4()<br>            #3) str(int(time.time()*1000))<br><br>            nonce = payload['nonce']<br><br>            # we use pyotp to generate OTP based on current system time<br>            # pyotp needs a base32 secret  It uses an alphabet of A–Z,<br>            # followed by 2–7. 0 and 1 are skipped due to their similarity<br>            # with the letters O and I<br>            # we store the common secret in .env file<br>            base32_secret = settings_basic_django.SECRET_KEY_BASE32_PYOTP<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            django_secret = settings_basic_django.SECRET_KEY<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # Now convert the nonce to base32<br>            # nonce.encode("UTF-8") - converts to bytes<br>            # base64.b32encode() gives byte string<br>            # .decode('utf-8') converts the byte string to string<br>            nonce_base32 = base64.b32encode(nonce.encode("utf-8")).decode('utf-8')<br><br>            django_secret_base32 = base64.b32encode(django_secret.encode("utf-8")).decode('utf-8')<br><br>            # the final secret we will use in pyotp is combination of<br>            # nonce_base32 + django_secret_base32 + base32_secret<br>            pyotp_secret = nonce_base32+django_secret_base32+base32_secret<br><br>            pyotp_secret_rep = re.sub(r'=', '', pyotp_secret)<br><br>            pin = pyotp.TOTP(pyotp_secret_rep,interval=settings_basic_django.TIMELIMIT_OTP).now()<br>            # ???<br><br>            # ??? Check the pin is valid<br>            if pin == form_data['OTP']:<br>            # ???<br><br>                # ???<br>                try:<br>                # ???<br><br>                    # ??? check for existing user and save<br>                    match = User.objects.get(email=payload['email'])<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    match.last_login2=time_now<br>                    match.recentdate_login_via_otp=time_now<br>                    match.save()<br>                    # ???<br>                    user_jwt_secret_main = match.jwt_secret<br><br>                    # ??? check match is active<br>                    if match.is_active:<br>                    # ???<br>                        #login(request,match,backend='django.contrib.auth.backends.ModelBackend')<br>                        logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    else:<br>                        messages_redirect.append(email + ' is not active')<br>                        response_data.update({'messages_redirect': messages_redirect})<br>                        response_data.update({'redirect': True})<br>                        response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_email')})<br>                        response_data.update(jwt_token)<br>                        response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                        return HttpResponse(<br>                              response_data_json_dumps,<br>                              status=200,<br>                              content_type="application/json"<br>                            )<br><br>                    #Get ip address<br>                    ip = settings.get_client_ip(request)<br><br>                    # get the action type<br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # Save in the session<br>                    match_UserSessionLog = UserSessionLog(<br>                        user_email=match.email,<br>                        ip_address = ip,<br>                        user = match,<br>                        otp_used_for_otplogin=form_data['OTP'],<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        # here we <br>                        created_time=time_now<br>                    )<br>                    match_UserSessionLog.save()<br>                    usersession_created_time = match_UserSessionLog.created_time<br>                    unique_id = match_UserSessionLog.unique_id<br>                    user_jwt_secret_session = match_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    # ???<br><br>                # ???<br>                except User.DoesNotExist:<br>                # ???<br>                    """<br>                        total length of Model_meta.get_fields(include_hidden=True):  32<br>                        [<br>                            "&lt;ManyToOneRel: admin.logentry&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_groups&gt;",<br>                            "&lt;ManyToOneRel: custom_user.user_user_permissions&gt;",<br>                            "&lt;ManyToOneRel: custom_user.usersessionlog&gt;",<br>                            [<br>                                "&lt;django.db.models.fields.AutoField: id&gt;",<br>                                "STR: custom_user.User.id"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login&gt;",<br>                                "STR: custom_user.User.last_login"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_superuser&gt;",<br>                                "STR: custom_user.User.is_superuser"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_staff&gt;",<br>                                "STR: custom_user.User.is_staff"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_joined&gt;",<br>                                "STR: custom_user.User.date_joined"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: password&gt;",<br>                                "STR: custom_user.User.password"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_passwd&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_passwd"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_login_via_otp&gt;",<br>                                "STR: custom_user.User.recentdate_login_via_otp"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: recentdate_password_change&gt;",<br>                                "STR: custom_user.User.recentdate_password_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_name&gt;",<br>                                "STR: custom_user.User.first_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: last_name&gt;",<br>                                "STR: custom_user.User.last_name"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.EmailField: email&gt;",<br>                                "STR: custom_user.User.email"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.BooleanField: is_active&gt;",<br>                                "STR: custom_user.User.is_active"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_recent_otp_used_for_pass_change&gt;",<br>                                "STR: custom_user.User.date_of_recent_otp_used_for_pass_change"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_otp_used_while_passlogin_create&gt;",<br>                                "STR: custom_user.User.date_of_otp_used_while_passlogin_create"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: date_of_first_otp_used_for_otplogin&gt;",<br>                                "STR: custom_user.User.date_of_first_otp_used_for_otplogin"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.TextField: about&gt;",<br>                                "STR: custom_user.User.about"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.CharField: location&gt;",<br>                                "STR: custom_user.User.location"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateField: birth_date&gt;",<br>                                "STR: custom_user.User.birth_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: modified_date&gt;",<br>                                "STR: custom_user.User.modified_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: creation_date&gt;",<br>                                "STR: custom_user.User.creation_date"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.DateTimeField: last_login2&gt;",<br>                                "STR: custom_user.User.last_login2"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.UUIDField: jwt_secret&gt;",<br>                                "STR: custom_user.User.jwt_secret"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: groups&gt;",<br>                                "STR: custom_user.User.groups"<br>                            ],<br>                            [<br>                                "&lt;django.db.models.fields.related.ManyToManyField: user_permissions&gt;",<br>                                "STR: custom_user.User.user_permissions"<br>                            ]<br>                        ]<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 228, in &lt;module&gt;<br>                            print(settings.pp_odir(Model_meta.get_fields(include_hidden=True),traceback.format_stack(limit=5)))<br><br><br><br>                        Lenght of c_dict[000_null_true***********************************************************************]  9<br>                        Lenght of c_dict[001_remaining***********************************************************************]  1<br>                        Lenght of c_dict[002_null_false_and_empty_strings****************************************************]  10<br>                        Lenght of c_dict[003_auto_now_add__OR__auto_now******************************************************]  2<br>                        Lenght of c_dict[004_auto_created********************************************************************]  5<br>                        Lenght of c_dict[005_default_not_empty_string********************************************************]  5<br>                        Total lenght of c_dict:  32<br>                        {<br>                            "000_null_true***********************************************************************": {<br>                                "birth_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "date_of_first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "date_of_recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "last_login": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "last_login2": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_otp": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_login_via_passwd": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                },<br>                                "recentdate_password_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "005_null": true,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true<br>                                }<br>                            },<br>                            "001_remaining***********************************************************************": {<br>                            @@@@"jwt_secret": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.UUIDField'&gt;",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false,<br>                                    "editable": false,<br>                                    "max_length": 32<br>                                }<br>                            },<br>                            "002_null_false_and_empty_strings****************************************************": {<br>                                "about": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.TextField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 500<br>                                },<br>                            @@@@"email": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.EmailField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 254,<br>                                    "unique": true<br>                                },<br>                                "first_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                            @@@@"first_otp_used_for_otplogin": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "groups": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                },<br>                                "last_name": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 150<br>                                },<br>                                "location": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "max_length": 30<br>                                },<br>                                "otp_used_while_passlogin_create": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "recent_otp_used_for_pass_change": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 6<br>                                },<br>                                "user_permissions": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.related.ManyToManyField'&gt;",<br>                                    "001_default": "",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": true,<br>                                    "many_to_many": true,<br>                                    "one_to_many": false,<br>                                    "one_to_one": false,<br>                                    "remote_field": "&lt;ManyToManyRel: custom_user.user&gt;"<br>                                }<br>                            },<br>                            "003_auto_now_add__OR__auto_now******************************************************": {<br>                                "creation_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "003_auto_now_add": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                },<br>                                "modified_date": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "004_auto_now": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "editable": false<br>                                }<br>                            },<br>                            "004_auto_created********************************************************************": {<br>                                "User_groups+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_groups.user"<br>                                    ]<br>                                },<br>                                "User_user_permissions+": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "hidden": true,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.User_user_permissions.user"<br>                                    ]<br>                                },<br>                                "id": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.AutoField'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": true,<br>                                    "primary_key": true,<br>                                    "unique": true<br>                                },<br>                                "logentry": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: admin.LogEntry.user"<br>                                    ]<br>                                },<br>                                "usersessionlog": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.reverse_related.ManyToOneRel'&gt;",<br>                                    "002_auto_created": true,<br>                                    "005_null": true,<br>                                    "editable": false,<br>                                    "many_to_many": false,<br>                                    "one_to_many": true,<br>                                    "one_to_one": false,<br>                                    "remote_field": [<br>                                        "&lt;django.db.models.fields.related.ForeignKey: user&gt;",<br>                                        "STR: custom_user.UserSessionLog.user"<br>                                    ]<br>                                }<br>                            },<br>                            "005_default_not_empty_string********************************************************": {<br>                                "date_joined": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.DateTimeField'&gt;",<br>                                    "001_default": [<br>                                        "datetime.datetime(2020, 3, 14, 16, 27, 44, 363244, tzinfo=&lt;UTC&gt;)",<br>                                        "STR: 2020-03-14 16:27:44.363244+00:00"<br>                                    ],<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                            @@@@"is_active": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_staff": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "is_superuser": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.BooleanField'&gt;",<br>                                    "001_default": false,<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": false,<br>                                    "007_blank": false<br>                                },<br>                                "password": {<br>                                    "000_class": "&lt;class 'django.db.models.fields.CharField'&gt;",<br>                                    "001_default": "pbkdf2_sha256$180000$YoBw24luwZAV$0ZL6l6/5DgeRJv7FEGMswDP4kGM+tE04rSfA3FDqYbQ=",<br>                                    "005_null": false,<br>                                    "006_empty_strings_allowed": true,<br>                                    "007_blank": false,<br>                                    "max_length": 128<br>                                }<br>                            }<br>                        }<br><br><br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/async_helpers.py", line 68, in _pseudo_sync_runner<br>                            coro.send(None)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3063, in run_cell_async<br>                            interactivity=interactivity, compiler=compiler, result=result)<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3254, in run_ast_nodes<br>                            if (await self.run_code(code, result, async_=asy)):<br>                          File "/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/lib/python3.7/site-packages/IPython/core/interactiveshell.py", line 3331, in run_code<br>                            exec(code_obj, self.user_global_ns, self.user_ns)<br>                          File "&lt;ipython-input-5-0bf2236d2c30&gt;", line 248, in &lt;module&gt;<br>                            print(settings.pp_odir(c_dict,traceback.format_stack(limit=5)))<br><br>                    """<br>                    # ??? Create a new user<br>                    time_now = timezone.now()<br>                    # if we do timezone.now(), (with a comma then it will save as tuple and will give error)<br>                    newuser = User(<br>                        email=payload['email'],<br>                        first_otp_used_for_otplogin=pin,<br>                        date_of_first_otp_used_for_otplogin=time_now,<br>                        last_login2=time_now,<br>                        recentdate_login_via_otp=time_now,<br>                        is_active=True<br>                        # we use timezone.now without brackets in default, so if dont convert to string it throws error<br>                        # expected string or bytes-like object @ dateparse.py in parse_datetime, line 106<br>                        #date_joined=time_now<br>                        )<br>                    newuser.save()<br>                    # ???<br><br>                    user_jwt_secret_main = newuser.jwt_secret<br><br>                    # Get the client ip:<br>                    ip = settings.get_client_ip(request)<br><br>                    action_type = ActionTypeForUserSessionLog.objects.get(action='login_by_otp')<br><br>                    # ??? Save in the session<br>                    new_UserSessionLog = UserSessionLog(<br>                        user_email=newuser.email,<br>                        ip_address = ip,<br>                        user = newuser,<br>                        otp_used_for_otplogin=pin,<br>                        action_type=action_type,<br>                        device_type=request.META['HTTP_USER_AGENT'],<br>                        created_time=time_now,<br>                    )<br><br>                    new_UserSessionLog.save()<br>                    # ???<br>                    unique_id = new_UserSessionLog.unique_id<br>                    user_jwt_secret_session = new_UserSessionLog.jwt_secret<br>                    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                    usersession_created_time = new_UserSessionLog.created_time<br><br>                # ??? Create a message to show that OTP is sent to email<br>                messages_redirect.append('Login Successful')<br>                # ???<br><br>                # ??? Create token authenticating a user<br>                django_secret = settings_basic_django.SECRET_KEY<br><br>                # we also use the secret form Userssion and User tables<br>                user_toke_secret = django_secret + user_jwt_secret_main.hex + user_jwt_secret_session.hex<br>                payload_token = {<br>                    'email': payload['email'],<br>                    'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>                }<br>                user_token = {<br>                    'token':jwt.encode(payload_token, user_toke_secret, algorithm='HS256').decode('utf-8'),<br>                    'unique_id':unique_id<br>                }<br>                # ???<br><br>                # ??? Add all the data to be sent to the response_data object<br>                response_data.update({'messages_redirect': messages_redirect})<br>                response_data.update({'redirect': True})<br>                response_data.update({'redirect_url': reverse('articles_namespace:articles')})<br>                response_data.update({"user_token":user_token})<br>                # ???<br><br>                # ??? Create json string<br>                response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>                # ???<br><br>                # ??? send the json_string of jwt_token<br>                return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br>                # ???<br><br>            # ??? if form is not valid<br>            form.add_error(None,"Form Error: Wrong OTP entered")<br>            remote_form = RemoteForm(form)<br>            remote_form_dict = remote_form.as_dict()<br>            # Errors in response_data['non_field_errors'] and response_data['errors']<br>            response_data.update({'form': remote_form_dict})<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': False})<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            response = HttpResponse(<br>                response_data_json_dumps,<br>                content_type="application/json"<br>            )<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            return response<br>            # ???<br>    else:<br>        #logger_custom_string.debug(request.GET.get('resendotp'))<br>        #logger_custom_string.debug(settings.pp_dict(request.GET))<br>        #logger_custom_string.debug('resendotp' in request.GET)<br><br>        if 'resendotp' in request.GET:<br><br>            import traceback<br>            form_data = json.loads(request.body)<br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br><br>            # CHECKING whether the session variable exists or not<br>            if 'jwt_token' in form_data:<br>                jwt_token = form_data['jwt_token']<br>            else:<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not found"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            # CHECKING jwt token and getting the payload<br>            try:<br>                # options = {<br>                #     'verify_exp': True,<br>                # }<br>                payload = jwt.decode(<br>                    jwt_token,<br>                    settings.SECRET_KEY,<br>                    True,<br>                    #options=options,<br>                )<br>                #logger_custom_string.debug(settings.pp_dict(payload))<br>            except Exception as e:  # NoQA<br>                #logger_custom_string.debug(str(e))<br>                status_code = 400<br>                message = "The request body is not valid."<br>                # You should log this error because this usually means your front end has a bug.<br>                # do you whant to explain anything?<br>                explanation = "jwt_token not valid"<br>                logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>                return HttpResponse(<br>                      json.dumps({'message':message,'explanation':explanation}),<br>                      status=status_code,<br>                      content_type="application/json"<br>                    )<br><br>            email = payload['email']<br><br>            pin, nonce = generate_pin_pyopt()<br>            # generate a random pin using crpto functions<br>            #pin = get_random_string(length=6, allowed_chars='1234567890')<br>            <br>            # EMAIL subject and BODY<br>            # for BODY we use a template and render it with parameters<br>            subject = pin + ': To Login via OTP'<br>            # We to create the email body. So we create a template and pass the required arguments.<br>            # render_to_string will render the template with the context values<br>            message = render_to_string('login_register_password/login_via_otp/email/login_otp_sendemail.html', {<br>                'email': email,<br>                'pin': pin<br>            })<br><br>            # USING CELERY TASK for sending email Asynchronously<br>            #match.email_user(subject, message). This will delay the response <br>            # So will do this task asynchronously using celery<br>            # We have created a celery task. Using it we will send the email.<br>            # The code does not have to wait till the email is sent<br>            send_email_task.delay(email,subject,message)<br><br>            payload = {<br>                'email': email,<br>                'nonce': nonce,<br>                'creation_time': str(datetime.datetime.now(tz=pytz.timezone('UTC')).isoformat())<br>            }<br><br>            jwt_token = {<br>                        'token':jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')<br>                        }<br><br>            logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>            # REDIRECTING TO A DIFFERENT VIEW ie. different URL<br>            logger_custom_string.debug(settings_basic_django.pp_odir(getattr(request, '_messages', []),traceback.format_stack(limit=5)))<br><br>            messages_redirect.append('OTP send to email: ' + email)<br>            response_data.update({'messages_redirect': messages_redirect})<br>            response_data.update({'redirect': True})<br>            response_data.update({'redirect_url': reverse('login_register_password_namespace:login_register_password_api_app_name:user_login_via_otp_form_otp')})<br>            response_data.update(jwt_token)<br>            response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br>            return HttpResponse(<br>                  response_data_json_dumps,<br>                  status=200,<br>                  content_type="application/json"<br>                )<br><br>        form = UserLoginViaOtpFormOTP()<br><br>    remote_form = RemoteForm(form)<br>    remote_form_dict = remote_form.as_dict()<br>    # Errors in response_data['non_field_errors'] and response_data['errors']<br>    response_data.update({'form': remote_form_dict})<br>    response_data.update({'messages_redirect': messages_redirect})<br>    response_data.update({'redirect': False})<br><br><br>    response_data_json_dumps = json.dumps(response_data, cls=DjangoJSONEncoder)<br><br><br><br>    response = HttpResponse(<br>        response_data_json_dumps,<br>        content_type="application/json"<br>    )<br>    import traceback<br>    logger_custom_string.debug(settings_basic_django.pp_odir(locals(), traceback.format_stack(limit=5)))<br>    return response<br><br><br>### #Basic one<br>### @csrf_exempt<br>### def user_login_via_otp_form_email(request):<br>###     response_data = {}<br>###     if request.method == 'GET':<br>###         # Get form definition<br>###         form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL})<br>###     elif request.method == 'POST':<br>###         form_data = json.loads(request.body)<br>###         logger_custom_string.debug(settings_basic_django.pp_odir(form_data,traceback.format_stack(limit=5)))<br>###         form = UserLoginViaOtpFormEmail(form_data)<br>###     html = "&lt;html&gt;&lt;body&gt;API TESTING&lt;/body&gt;&lt;/html&gt;"<br>###     return HttpResponse(html)<br><br><br>                <br><br><br><br></td></tr></tbody></table>

 * ## \[code\] urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path, include<br>from . import views<br><br>app_name='login_register_password_api_app_name'<br><br>urlpatterns = [<br>    path('user_login_via_otp_form_email',views.user_login_via_otp_form_email, name='user_login_via_otp_form_email'),<br>    path('user_login_via_otp_form_otp',views.user_login_via_otp_form_otp, name='user_login_via_otp_form_otp')<br>]<br></td></tr></tbody></table>

 * ## \[image\] urls.py

     * ![](images/image24.png)

 * ## \[image\] curl commands: Checking the urls using curl:

     * ![](images/image129.png)![](images/image104.png)![](images/image9.png)![](images/image345.png)![](images/image74.png)![](images/image160.png)![](images/image316.png)![](images/image175.png)![](images/image353.png)![](images/image332.png)![](images/image75.png)![](images/image201.png)

 * ## \[code\] curl commands:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td># view as bash syntax in sublime text<br><br>CURL FOR POSTING DATA:<br>--location helps to auto redirect<br>-- NO need to use --request POST<br>-- data-raw will automatically start POST<br><br>#####<br>POST email with improper json string: FOR json.loads(request.body)- Exception\nExpecting property name enclosed in double quotes: line 2 column 1 (char 2)<br><br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_email' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>email:"test@test.com"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br><br>OUTPUT:<br><br>{<br>  "message": "The request body is not valid.",<br>  "explanation": "json.loads(request.body): Expecting property name enclosed in double quotes: line 2 column 1 (char 2)"<br>}<br><br><br>#####<br>POST email: with form errors<br><br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_email' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"email" :"testtest.com"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br><br>OUTPUT: <br><br>{<br>  "form": {<br>    "title": "UserLoginViaOtpFormEmail",<br>    "errors": {<br>      "email": [<br>        "Enter a valid email address."<br>      ]<br>    },<br>    "non_field_errors": [],<br>    "label_suffix": ":",<br>    "is_bound": true,<br>    "prefix": null,<br>    "fields": {"email":{"title":"EmailField","required":true,"label":"Email address","initial":null,"help_text":"Please Enter valid Email Address","error_messages":{"required":"This field is required."},"widget":{"title":"TextInput","is_hidden":false,"needs_multipart_form":false,"is_localized":false,"is_required":true,"attrs":{"maxlength":"254"},"input_type":"text"},"max_length":254,"min_length":null}},<br>    "fieldsets": [],<br>    "ordered_fields": [<br>      "email"<br>    ],<br>    "data": {<br>      "email": "testtest.com"<br>    }<br>  },<br>  "messages_redirect": [],<br>  "redirect": false<br>}<br><br>#####<br>POST email<br><br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_email' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"email" :"test@test.com"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "messages_redirect": [<br>    "OTP send to email: test@test.com"<br>  ],<br>  "redirect": true,<br>  "redirect_url": "/login_register_password/api/user_login_via_otp_form_otp",<br>  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6IlE2ak1jUVpDVzVkd2xyNm5uSW00akx5LXU1UlhWX01zeVFSbUQ1ejBHYk0iLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzoxMTo0NC4zMjU4MzIrMDA6MDAifQ.H57aaYVbJU1hBZ0OJmGZNkMVH4us31Y4KOupITYuuKE"<br>}<br><br>#####<br>GET email form to get OTP<br><br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_email' \<br>--header 'Content-Type: application/json' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br><br><br>######<br>GET otp form<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br><br>OUTPUT:<br><br>{<br>  "form": {<br>    "title": "UserLoginViaOtpFormOTP",<br>    "errors": {},<br>    "non_field_errors": [],<br>    "label_suffix": ":",<br>    "is_bound": false,<br>    "prefix": null,<br>    "fields": {"otp_loginconfirm":{"title":"CharField","required":true,"label":"Otp","initial":null,"help_text":"Please Enter valid OTP sent to your Email","error_messages":{"required":"This field is required."},"widget":{"title":"TextInput","is_hidden":false,"needs_multipart_form":false,"is_localized":false,"is_required":true,"attrs":{"maxlength":"6"},"input_type":"text"},"max_length":6,"min_length":null}},<br>    "fieldsets": [],<br>    "ordered_fields": [<br>      "otp_loginconfirm"<br>    ],<br>    "data": {<br>      "otp_loginconfirm": null<br>    }<br>  },<br>  "messages_redirect": [],<br>  "redirect": false<br>}<br><br><br>#####<br>POST OTP form  -- mistake in json<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6ImVSZXpWd3NicUNWd3BralA2LU1tNk1wM1Y5VU1Pakt3QVdpNmhzTXcyTGMiLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wMy0yOVQwOTo1MzoxNy40NTM5NTArMDA6MDAifQ.oqKkM9hntOlr2xflSFwZPrCOmQ5g0DoBJo3XRC0cOYY",<br>OTP:"727966"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "message": "The request body is not valid.",<br>  "explanation": "json.loads(request.body): Expecting property name enclosed in double quotes: line 3 column 1 (char 273)"<br>}<br><br><br>##### <br>POST OTP form -- OTP param not provided<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6ImVSZXpWd3NicUNWd3BralA2LU1tNk1wM1Y5VU1Pakt3QVdpNmhzTXcyTGMiLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wMy0yOVQwOTo1MzoxNy40NTM5NTArMDA6MDAifQ.oqKkM9hntOlr2xflSFwZPrCOmQ5g0DoBJo3XRC0cOYY"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "message": "The request body is not valid.",<br>  "explanation": "OTP param is not found"<br>}<br><br>#####<br>POST OTP form -- jwt_token not provided<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"OTP":"727966"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "message": "The request body is not valid.",<br>  "explanation": "jwt_token not found"<br>}<br><br>#####<br>GET OTP form  -- ask to resend OTP<br>curl --verbose --location --request GET 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp?resendotp=' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6ImVSZXpWd3NicUNWd3BralA2LU1tNk1wM1Y5VU1Pakt3QVdpNmhzTXcyTGMiLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wMy0yOVQwOTo1MzoxNy40NTM5NTArMDA6MDAifQ.oqKkM9hntOlr2xflSFwZPrCOmQ5g0DoBJo3XRC0cOYY"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "messages_redirect": [<br>    "OTP send to email: test@test.com"<br>  ],<br>  "redirect": true,<br>  "redirect_url": "/login_register_password/api/user_login_via_otp_form_otp",<br>  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6ImZlaVl2amtFUDVoanhJdE9lejVtSE1qNTgtZnZlYm5xVnFWVnVrcGpLeVUiLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzoyNDozNi40NDc1MzIrMDA6MDAifQ.s_t8wIsfYcAdopxS98mgS9kZC4g8Jfz_0wL5Fsr0maE"<br>}<br><br><br>#####<br>POST OTP form if OTP is expired<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6ImVSZXpWd3NicUNWd3BralA2LU1tNk1wM1Y5VU1Pakt3QVdpNmhzTXcyTGMiLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wMy0yOVQwOTo1MzoxNy40NTM5NTArMDA6MDAifQ.oqKkM9hntOlr2xflSFwZPrCOmQ5g0DoBJo3XRC0cOYY",<br>"OTP":"727966"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "form": {<br>    "title": "UserLoginViaOtpFormOTP",<br>    "errors": {<br>      "__all__": [<br>        "OTP expired, Click on resend OTP"<br>      ]<br>    },<br>    "non_field_errors": [<br>      "OTP expired, Click on resend OTP"<br>    ],<br>    "label_suffix": ":",<br>    "is_bound": true,<br>    "prefix": null,<br>    "fields": {"otp_loginconfirm":{"title":"CharField","required":true,"label":"Otp","initial":null,"help_text":"Please Enter valid OTP sent to your Email","error_messages":{"required":"This field is required."},"widget":{"title":"TextInput","is_hidden":false,"needs_multipart_form":false,"is_localized":false,"is_required":true,"attrs":{"maxlength":"6"},"input_type":"text"},"max_length":6,"min_length":null}},<br>    "fieldsets": [],<br>    "ordered_fields": [<br>      "otp_loginconfirm"<br>    ],<br>    "data": {<br>      "otp_loginconfirm": "727966"<br>    }<br>  },<br>  "messages_redirect": [],<br>  "redirect": false<br>}<br><br>#####<br>POST OTP form OTP invalid<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6IjlpeFA2cWhWLTBZazBYZE52V2xyWGFSS09aeDZ3MGkxcHAtYm1LQ0hZbGciLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzoyODo0OS44MDEwMTUrMDA6MDAifQ.R0tJ0Ma6slwG-1U5CHaBTQajnpXkM7euB04SUimSvLo",<br>"OTP":"848412"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "form": {<br>    "title": "UserLoginViaOtpFormOTP",<br>    "errors": {<br>      "__all__": [<br>        "Form Error: Wrong OTP entered"<br>      ]<br>    },<br>    "non_field_errors": [<br>      "Form Error: Wrong OTP entered"<br>    ],<br>    "label_suffix": ":",<br>    "is_bound": true,<br>    "prefix": null,<br>    "fields": {"otp_loginconfirm":{"title":"CharField","required":true,"label":"Otp","initial":null,"help_text":"Please Enter valid OTP sent to your Email","error_messages":{"required":"This field is required."},"widget":{"title":"TextInput","is_hidden":false,"needs_multipart_form":false,"is_localized":false,"is_required":true,"attrs":{"maxlength":"6"},"input_type":"text"},"max_length":6,"min_length":null}},<br>    "fieldsets": [],<br>    "ordered_fields": [<br>      "otp_loginconfirm"<br>    ],<br>    "data": {<br>      "otp_loginconfirm": "848412"<br>    }<br>  },<br>  "messages_redirect": [],<br>  "redirect": false<br>}<br><br>#####<br>POST OTP form jwt_token invalid<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"AiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6IjlpeFA2cWhWLTBZazBYZE52V2xyWGFSS09aeDZ3MGkxcHAtYm1LQ0hZbGciLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzoyODo0OS44MDEwMTUrMDA6MDAifQ.R0tJ0Ma6slwG-1U5CHaBTQajnpXkM7euB04SUimSvLo",<br>"OTP":"848412"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br>OUTPUT:<br><br>{<br>  "message": "The request body is not valid.",<br>  "explanation": "jwt_token not valid"<br>}<br><br><br>#####<br>POST OTP form with valid jwt_token and OTP<br>curl --verbose --location 'http://127.0.0.1:8000/login_register_password/api/user_login_via_otp_form_otp' \<br>--header 'Content-Type: application/json' \<br>--data-raw '{<br>"jwt_token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJub25jZSI6Ii1JVTFvTDJubWFRQ2l1OVNVbkJ3Uk1PSnpYSkpwZXREMS1Lbk82eU9jNG8iLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzozMjo1NC41OTc5MTcrMDA6MDAifQ.JIVYeuGNO6LaM55hcTSpdgG2nh_avVixi-n-pLtMkwY",<br>"OTP":"363011"<br>}' | tee ~/test.json ~/test.html; firefox ~/test.json ~/test.html<br><br><br>OUTPUT:<br>{<br>  "messages_redirect": [<br>    "Login Successful"<br>  ],<br>  "redirect": true,<br>  "redirect_url": "/",<br>  "user_token": {<br>    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InRlc3RAdGVzdC5jb20iLCJjcmVhdGlvbl90aW1lIjoiMjAyMC0wNC0wM1QxMzozMzo1Ni44Nzc5OTMrMDA6MDAifQ.gb1PvrkfIgg4digSml32aofv1BjXTWouclQv_C3ztGw",<br>    "unique_id": "edd1e80c-c875-4ffe-8587-02a3c54e226c"<br>  }<br>}<br><br></td></tr></tbody></table>

 * ## How to set logging time to IST

     * ![](images/image307.png)

 * ## Adding absolute path and Method in verbose in logging in settings.py

     * ![](images/image184.png)

* # Miscellaneous

 * ## Webpack Main Concepts

     * ### Entry

       * |                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

       * | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

       * | The entry point is the module, which webpack uses to start building its internal dependency graph. From there, it determines which other modules and libraries that entry point depends on (directly and indirectly) and includes them in the graph until no dependency is left. By default, the entry property is set to ./src/index.js, but we can specify a different module (or even multiple modules) in the webpack configuration file. |

     * ### Output

       * |                                                                                                                                                                                                                                                                                                                                                                        |

       * | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

       * | The output property instructs webpack where to emit the bundle(s) and what name to use for that file(s). The default value for this property is ./dist/main.js for the main bundle and ./dist for other generated files — such as images, for example. Of course, we can specify different values in the configuration depending on our needs. |

     * ### Loaders

       * |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

       * | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

       * | By default, webpack only understands JavaScript and JSON files. To process other types of files and convert them into valid modules, webpack uses loaders. Loaders transform the source code of non-JavaScript modules, allowing us to preprocess those files before they’re added to the dependency graph. For example, a loader can transform files from a CoffeeScript language to JavaScript or inline images to data URLs. With loaders we can even import CSS files directly from our JavaScript modules. |

     * ### Plugins

       * |                                                                                                                                                                                                            |

       * | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

       * | Plugins are used for any other task that loaders can’t do. They provide us with a wide range of solutions about asset management, bundle minimization and optimization, and so on. |

     * ### Mode

       * |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

       * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

       * | Typically, when we develop our application we work with two types of source code — one for the development build and one for the production build. Webpack allows us to set which one we want to be produced by changing the mode parameter to development, production or none. This allows webpack to use built-in optimizations corresponding to each environment. The default value is production. The none mode means that there won’t be used any default optimization options. |

 * ## Webpack: how to have multiple entries and outputs and easily use them in template

     * [https://github.com/owais/django-webpack-loader/issues/177](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader/issues/177&sa=D&ust=1585972459443000)

     * polls app: we want to have two bundled js for index and questions html pages.

     * Project structure:

     * ![](images/image49.png)

     * ### \[code\] settings.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>STATIC_URL = '/static/'<br><br>WEBPACK_LOADER = {<br>    'DEFAULT': {<br>        'BUNDLE_DIR_NAME': '',<br>        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>        # '/home/web_dev/krishnacook_pipenv/webpack-stats.json'<br>    }<br>}<br></td></tr></tbody></table>

     * ### \[code\] Webpack.config.js:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var path = require("path");<br>var webpack = require('webpack');<br>var BundleTracker = require('webpack-bundle-tracker');<br><br>module.exports = {<br>  context: __dirname,<br><br>// mention the path in the key name (refer to the webpack multiple entries<br><br>  entry: {<br>    'polls/bundles/index':  './src/polls/static/polls/js/index',<br>    'polls/bundles/questions':  './src/polls/static/polls/js/questions',<br>   },<br><br>  output: {<br>    path: path.join(__dirname, '/src/polls/static/'),<br>    filename: "[name]-[hash].js",<br>  },<br><br>  // output: {<br>  //     path: path.resolve('./src/polls/static/bundles/'),<br>  //     filename: "[name]-[hash].js",<br>  // },<br><br>  plugins: [<br>    new BundleTracker({filename: './src/webpack-stats.json'}),<br>  ],<br>  module: {<br>    rules: [<br>      {<br>        test: /\.js$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>};<br></td></tr></tbody></table>

     * ### \[image\] webpack.config.js

       * ![](images/image293.png)![](images/image283.png)

     * ### \[code\] templates/polls/index.html

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{% load render_bundle from webpack_loader %}<br>&lt;!DOCTYPE html&gt;<br>&lt;html&gt;<br> &lt;head&gt;<br> &lt;meta charset="UTF-8"&gt;<br> &lt;title&gt;Example&lt;/title&gt;<br> &lt;/head&gt;<br> &lt;body&gt;<br> &lt;div id="react"&gt;&lt;/div&gt;<br> {% render_bundle 'polls/bundles/index' %}<br> &lt;/body&gt;<br>&lt;/html&gt;<br>then it points to http://127.0.0.1:8000/static/polls/bundles/index-90…..js<br></td></tr></tbody></table>

     * ### \[code\] polls/urls.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.urls import path<br><br>from .views import PollQuestions, index<br><br><br>urlpatterns = [<br>    path('', index, name='index'),<br>    path('questions/', PollQuestions.as_view(), name='questions')<br>]<br></td></tr></tbody></table>

     * ### \[code\] polls/views,py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.shortcuts import render<br><br># Create your views here.<br>from django.views import View<br><br>from .models import Question<br><br><br>def index(request):<br>    return render(request, 'polls/index.html')<br><br><br>class PollQuestions(View):<br>    title = "Questions"<br>    template = 'polls/questions.html'<br><br>    def get(self, request):<br>        questions = list(Question.objects.values('pk', 'question_text'))<br><br>        context = {<br>            'question_text': self.title,<br>            'props': questions,<br>        }<br><br>        return render(request, self.template, context)<br></td></tr></tbody></table>

     * ### \[code\] polls/static/polls/js/index.js

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import React from 'react'<br>import ReactDOM from 'react-dom'<br><br><br>function Welcome(props) {<br>  return &lt;h1&gt;Hello, {props.name}&lt;/h1&gt;;<br>}<br><br>const element = &lt;Welcome name="world" /&gt;;<br>ReactDOM.render(<br>  element,<br>  document.getElementById('react')<br>);<br></td></tr></tbody></table>

 * ## How to integrate Django API project with nodejs and react on frontend?. Why not to use SPA

     * https://stackoverflow.com/questions/42943160/how-to-integrate-django-api-project-with-nodejs-and-react-on-frontend

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Solution was to abandon the single page app model, and instead let Django serve each page individually, with a root React component for each page. Our base site components that don’t change between pages (e.g. navbar, footer) are provided by the Django templates, and the content specific to each page (e.g. poker interface, leaderboard) are composed within React.<br><br><ol><li>Abandon the SPA, why would you say such a horrible thing?! Single page apps are not always the solution, we’ve gained stability (bugs are limited to only one page), easier debugging, easy search engine indexing, and easier static page management by having page boilerplate and routing handled by Django</li></ol><br><ol start="2"><li>It’s much easier to create non-React pages for static content (e.g. about page, login page) when you have all your page boilerplate in Django templates</li></ol><br><ol start="3"><li>No need to deal with React routers, the History API, or async fetching of page content behind the scenes (more on how we do page hotloading without refreshes in a later post)</li></ol></td></tr></tbody></table>

 * ## Webpack: Multiple entry points:

     * To use multiple entry points you can pass an object to the entry option. Each value is treated as an entry point and the key represents the name of the entry point.

     * When using multiple entry points you must override the default output.filename option. Otherwise each entry point would write to the same output file. Use \[name\] to get the name of the entry point.

     * Minimal example configuration

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>        entry: {<br>                a: "./a",<br>                b: "./b",<br>                c: ["./c", "./d"]<br>        },<br>        output: {<br>                path: path.join(__dirname, "dist"),<br>                filename: "[name].entry.js"<br>        }<br>}<br></td></tr></tbody></table>

 * ## Webpack: path as the entry name: How to set multiple file entry and output in project with webpack?

     * If you want to output to multiple directories, you can use the path as the entry name. For example if you want this directory structure:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>apps<br>├── dir1<br>│   └── js<br>│       ├── main.js [entry 1]<br>│       └── bundle.js [output 1]<br>└── dir2<br>    ├── index.js [entry 2]<br>    └── foo.js [output 2]<br></td></tr></tbody></table>

     * Then try this in your module.exports:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>  entry: {<br>    'dir1/js/bundle': path.resolve(__dirname, '/apps/dir1/js/main.js'),<br>    'dir2/foo' : path.resolve(__dirname, '/apps/dir2/index.js')<br>  },<br>  output: {<br>    path: path.resolve(__dirname, '/apps'),<br>    filename: '[name].js'<br>  },<br>  ...<br>}<br><br>Here  'dir1/js/bundle' is [name] of the entry point. <br></td></tr></tbody></table>

     * Here the important thing is \[name\] and path  (Use \[name\] to get the name of the entry point)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#guranga<br>Its like <br>[path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name].js'<br>] == [path]+[name].js  == [/apps/]+[dir1/js/bundle].js = /apps/dir1/js/bundle.js<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>and then stats file become:<br><br>{<br>  "status": "done",<br>  "chunks": {<br><br>    # this is same as the entry name<br>    "dir1/js/bundle": [<br>      {<br><br>        # here name is derived from filename: '[name].js' ([name] is entry index name)<br>        "name": "dir1/js/bundle.js",<br><br>        # here path is derived from [path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name].js'] = [path] + [name].js <br>        "path": "/apps/dir1/js/bundle.js"<br><br>      }<br>    ],<br>    "dir2/foo": [<br>      {<br>        "name": "dir2/foo.js",<br>        "path": "/apps/dir2/foo.js"<br>      }<br>    ]<br>  }<br>}<br><br></td></tr></tbody></table>

 * ## Webpack: multiple output paths

     * Webpack does support multiple output paths.

     * Set the output paths as the entry key. And use the name as output template.

     * webpack config:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>entry: {<br>    'module/a/index': 'module/a/index.js',<br>    'module/b/index': 'module/b/index.js',<br>},<br>output: {<br>    path: path.resolve(__dirname, 'dist'),<br>    filename: '[name].js'<br>}<br></td></tr></tbody></table>

     * generated:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>dist<br>└── module<br>    ├── a<br>    │   └── index.js<br>    └── b<br>        └── index.js<br></td></tr></tbody></table>

 * ## Django-webpack-loader: [https://github.com/owais/django-webpack-loader](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&sa=D&ust=1585972459483000)

     * https://owais.lone.pw/blog/webpack-plus-reactjs-and-django/

     * Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

     * Install webpack-bundle-tracker and django-webpack-loader

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>npm install --save-dev webpack-bundle-tracker<br><br>pipenv install django-webpack-loader<br></td></tr></tbody></table>

     * If you use the --save or --save-dev flag when installing a package, it’ll save the packages as dependencies in the package.json file.

     * To reinstall the packages, all you need to is run npm install

     * The packages will be installed locally specific to your project under a directory called node\_modules like virtualenv. To install a package globally, all you need to do is to use -g with npm install.

     * ### setup npm in the root of your django project:

       * This will generate a file called package.json in your project root.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>npm init<br></td></tr></tbody></table>

     * ### Npm dependencies

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>WEBPACK RELATED:<br><ol><li>webpack: we will need webpack package</li></ol><br><ol start="2"><li>Webpack-bundle-tracker: plugin to extract useful information from webpack and store it in as json in a file. This file will act as the link between webpack and django.</li></ol><br>Installation:<br>npm install --save-dev webpack webpack-bundle-tracker <br><br><br>REACTJS RELATED:<br><ol start="3"><li>React: Reactjs is a JavaScript library to build UI and is one of the widely used and popular JavaScript library in today’s date.</li></ol><br><ol start="4"><li>React-dom: We will be needing one more package called react-dom package to render the DOM.</li></ol><br>Installation:<br>npm install --save-dev react react-dom<br><br>BABEL RELATED:<br><ol start="5"><li>babel-core: babel transpile ES6 code to ES5</li></ol><br><ol start="6"><li>babel-loader: This is a webpack helper which allows to transpile Javascript files with babel and webpack. It uses babel under the hood</li></ol><br><ol start="7"><li>babel/preset-env: It determines which features needs to be transformed to run within different browsers or runtime versions. This is also known as browser polyfills</li></ol><br><ol start="8"><li>babel/preset-react: It is used to transform all your React JSX into functions.</li></ol><br>Installation: <br>npm install --save-dev @babel/core babel-loader @babel/preset-env @babel/preset-react<br><br>touch .babelrc<br>{<br>  "presets": ["@babel/preset-env", "@babel/preset-react"]<br>}<br><br>For webpack loaders:<br><br>module.exports = {<br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  }<br>}<br><br><br>https://blog.usejournal.com/setting-up-react-webpack-4-babel-7-from-scratch-2019-b771dca2f637<br></td></tr></tbody></table>

     * ### Installing npm packages:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>npm install --save-dev webpack webpack-bundle-tracker <br><br>npm install --save-dev react react-dom<br><br>npm install --save-dev @babel/core babel-loader @babel/preset-env @babel/preset-react<br></td></tr></tbody></table>

       * #### Note for babel:

         * We also need to setup our babel config file, create a new file in the root directory called .babelrc and write the following configuration to it

         * .babelrc

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>  "presets": ["@babel/preset-env", "@babel/preset-react"]<br>}<br><br>OR<br><br>{<br>  "presets": ["@babel/env", "@babel/react"]<br>}<br><br></td></tr></tbody></table>

         * The above configuration will ensure that babel transpiles our react code, which is JSX and any other ES6+ code we have to ES5 code.

         * Add the babel-loader to webpack.config.js

         * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>module.exports = {<br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  }<br>}<br></td></tr></tbody></table>

         * What the above configuration does is that for every file with a js or jsx extension, excluding the node\_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. With this done, lets head over to writing our react component.

         * https://scotch.io/@deityhub/settingup-reactjs-using-webpack-4-and-babel-7-the-definitive-guide

     * ### save vs save-dev

       * |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

       * | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

       * | --save saves the packages you install as dependencies of your package. The packages that must be installed in order to run your package. --save-dev saves the packages as build dependencies, the packages that must be installed to hack on your package. Since we are not going to be publishing a real npm package, either one works. I like to use –save-dev as I only need the packages to build my bundles. Whatever the bundle depends on is included in the bundle itself. |

     * ### Create webpack config

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>mkdir -p assets/js<br>touch webpack.config.js<br>touch assets/js/index.js<br></td></tr></tbody></table>

     * ### Create webpack config

       * Let’s create a simple webpack config to load .jsx files using babel and use the webpack-bundle-tracker plugin to extract information to webpack-stats.json. More on webpack configuration here.

       * Note:  loaders used for jsx & plugins used for webpack-stats.json

       * Note:  We refer to ./assets/js/index as the entry point of our app in webpack.config.js which will look for index, index.js or index.jsx because we’ve added these three extensions to our webpack config under the key resolve.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var path = require("path")<br>var webpack = require('webpack')<br>var BundleTracker = require('webpack-bundle-tracker')<br><br>module.exports = {<br>  context: __dirname,<br><br>  entry: './assets/js/index', // entry point of our app. assets/js/index.js should require other js modules and dependencies it needs<br><br>  output: {<br>      path: path.resolve('./assets/bundles/'),<br>      filename: "[name]-[hash].js",<br>  },<br><br>  plugins: [<br>    new BundleTracker({filename: './webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    loaders: [<br>      { test: /\.jsx?$/, exclude: /node_modules/, loader: 'babel-loader'}, // to transform JSX into JS<br>    ],<br>  },<br><br>  resolve: {<br>    modulesDirectories: ['node_modules', 'bower_components'],<br>    extensions: ['', '.js', '.jsx']<br>  },<br>}<br></td></tr></tbody></table>

     * ### Directory Structure:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>root/<br>├── manage.py<br>├── package.json<br>│── webpack.config.js<br>│── webpack-stats.json # generated by webpack<br>├── node_modules/ #contains our JS dependencies. This is like python's virtualenv directory<br>├── assets/ #added to STATICFILES_DIRS<br>│   └── js/ # contains out JS source code<br>│   └── bundles/ # generated by webpack<br></td></tr></tbody></table>

     * ### Compiling our first bundle

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Binaries shipped with node packages are installed to node_modules/.bin/ and it not added to $PATH automatically so we need to use full paths to the binaries.<br><br>./node_modules/.bin/webpack --config webpack.config.js<br></td></tr></tbody></table>

       * This should create bundle at assets/bundles/main-\[hash\].js. This is good but we don’t want to create bundles manually every time we make changes to our code.

     * ### Watch mode:

       * |                                                                                         |

       * | --------------------------------------------------------------------------------------- |

       * | ./node\_modules/.bin/webpack --config webpack.config.js --watch |

       * This will leave the compiler running and compile bundles automatically when you change any of your source files. You’ll need to restart it if you make any changes to the webpack configuration though.

* # How to Take Screen shot of terminator:

     * We want to take the screenshot of the terminator output. So we have to capture screen and scroll and again capture screen.

 * ## First we have to manually resize the terminator so that its cursor and the edge matche

     * ### \[image\] wrong way to resize the terminator

       * ![](images/image320.png)

     * ### \[code\] correct way to resize the terminator

       * ![](images/image186.png)

 * ## Create a file called terminator\_screenshot.sh and copy the script into it

     * ### \[code\] terminator screen shot script

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>set -x -o verbose;<br>export DISPLAY=:0.0 &amp;&amp;<br><br>#### important<br># Before running this script ensure that the size of the terminal is manually fit <br># to the cursor button.<br><br># the below is to get the recent seen window in a group of windows<br>xdotool search  --desktop 0 --class Terminator<br>windowid=$(xdotool search  --desktop 0 --class Terminator | awk 'END{print}'); <br>width_ter=`xdotool getwindowgeometry $windowid | awk '/Geometry/' | awk '{match($0,/Geometry: ([0-9]+)x([0-9]+)/,a); print a[1]}'`<br>height_ter=`xdotool getwindowgeometry $windowid | awk '/Geometry/' | awk '{match($0,/Geometry: ([0-9]+)x([0-9]+)/,a); print a[2]}'`<br>echo $width_ter<br>echo $height_ter<br><br>xdotool windowactivate ${windowid} &amp;&amp;<br><br>#crop_a=$((21)) # this is for not tabs<br>#crop_a=$((0)) # this is for not tabs<br>crop_a=$((21+36)) # this is for tabs<br>crop_b=$((1)) # this is for tabs<br><br>DIR="/home/simha/terminator_screenshots"<br># init<br># look for empty dir <br>if [ "$(ls -A $DIR)" ]; then<br>   echo "Take action $DIR is not Empty"<br>else<br>   echo "$DIR is Empty"<br>   filename="$(date +%Y-%m-%d-%H_%M_%S).png"<br>   echo $filename<br>   import -window ${windowid} -crop +0+${crop_a} -crop +0-${crop_b} /home/simha/terminator_screenshots/${filename}<br>fi<br><br><br>sleep 1<br><br>echo "MotionNotify 508 251" &gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrPress Shift_L" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "Delay 400" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrPress Prior" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrRelease Prior" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "Delay 408" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrRelease Shift_L" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br><br>xmacroplay &lt; "/home/simha/.public_html/xmacros_terminator_screenshot"<br><br>filename="$(date +%Y-%m-%d-%H_%M_%S).png"<br>echo $filename<br>import -window ${windowid} -crop +0+${crop_a} -crop +0-${crop_b}  /home/simha/terminator_screenshots/${filename}<br><br>gwenview /home/simha/terminator_screenshots/${filename}<br><br></td></tr></tbody></table>

     * ### \[image\] terminator screenshot script

       * ![](images/image191.png)

 * ## Create a keyboard shortcut for this script in KDE desktop env

     * In kde got to edit applications and create a keyboard shortcut for this script. (i have created WIN + h)

 * ## Start taking screenshots

     * Now after resizing the terminator properly press the shortcut key and it will take a screenshot and move the screen up. If we want to take more screen shot again press the shortcut key and keep doing this till the time you want.

 * ## Combine the screenshots

     * All the screenshots will be stored in the folder /home/simha/terminator\_screenshots

     * ### \[code\] To combine all the images into one use the following command:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ convert -append $(ls -1 *.png | sort -r) out.png<br></td></tr></tbody></table>

     * ### \[image\] to combine all the images into one

       * ![](images/image207.png)

 * ## Break images into multiple images for the purpose of using them in google docs

     * If the image is long we have to break it into multiple images. Else google docs when converting it into html it will show low res images. For that we run the following script

     * ### \[code\] splitting the images vertically with aspect ratio of 900:600

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ filename="git_stashing_usage.png"               <br>rm -rf ~/croped &amp;&amp;<br>mkdir ~/croped &amp;&amp;<br>width=`identify -format '%w' ${filename}`<br>echo "width= $width"<br>height=`identify -format '%h' ${filename}`<br>echo "height= $height"<br><br>a=`echo "scale=10; ((900/$width) * $height)/600" | bc`<br>echo $a<br><br>rem=`echo "scale=1; $a % 1" | bc`<br>echo $rem<br>int1=`echo "($height*$width)/(600*900)" | bc`<br>echo $int1<br>int2=$(( $int1 + 1))<br>echo $int2<br><br>st=$((`echo "$rem &lt; 0.3"| bc`))<br>echo "st= $st"<br>if [ $st -eq 1 ]; then<br>        echo "$rem &lt; 0.3"<br>    convert -crop 1x${int1}+0+8@ ${filename} ~/croped/crop_grid_%d.png<br>else<br>        echo "$rem &gt; 0.3"<br>        convert -crop 1x${int2}+0+8@ ${filename} ~/croped/crop_grid_%d.png<br>fi<br><br>pcmanfm /home/simha/croped<br></td></tr></tbody></table>

     * ### \[image\] splitting images vertically

       * ![](images/image12.png)

 * ## Paste them into the google docs:

     * Once the images are split then we can paste them into the google docs.

 * ## Using gimp to split images using guides and keep required images and then combine them.

     * Sometimes we want to split an image using guides. This can be done using gimp. Go to Filters \> web \> Slice. Then save the split images into a folder.

     * Delete the unwanted images and then combine them using

     * $ convert -append $(ls -1 \*.png) out.png

 * ## Django putting all the apps in subfolder:

     * [https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error](https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&sa=D&ust=1585972459533000)[r](https://www.google.com/url?q=https://stackoverflow.com/questions/3948356/how-to-keep-all-my-django-applications-in-specific-folder&sa=D&ust=1585972459533000)

     * https://stackoverflow.com/questions/3948356/how-to-keep-all-my-django-applications-in-specific-folder

     * ### Question:

       * I have a Django project, let's say "project1". Typical folder structure for applications is:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>/project1/<br>         /app1/<br>         /app2/<br>         ...<br>         __init__.py<br>         manage.py<br>         settings.py<br>         urls.py<br></td></tr></tbody></table>

       * What should I do if I want to hold all of my applications in some separate folder, 'apps' for example? So that structure should look like the following:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>/project/<br>         apps/<br>              app1/<br>              app2/<br>              ...<br>         __init__.py<br>         manage.py<br>         settings.py<br>         urls.py<br></td></tr></tbody></table>

     * ### Answer:

       * No matter if you have just created your project or if you want to move your apps, create the apps subdirectory that should contain your apps. The trick is to add an \_\_init\_\_.py to that directory.

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>mkdir apps<br>touch apps/__init__.py<br>Touch apps/models.py<br></td></tr></tbody></table>

       * You need both these files under your app folder:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>__init__.py<br>models.py<br></td></tr></tbody></table>

       * They can be empty. Why we need  models.py 

       * [https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder](https://www.google.com/url?q=https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder&sa=D&ust=1585972459539000)

       * [https://stackoverflow.com/a/6649433/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/6649433/2897115&sa=D&ust=1585972459540000)

       * It didn't need any database tables, but not having a models.py meant that the test runner was not picking it up.

       * For sake of test to work then below works

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>python2 manage.py test apps/appname1<br></td></tr></tbody></table>

       * Now you can move your existing apps into the apps subdirectory. If you would like to create a new one instead here are the commands:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>python manage.py mysecondapp<br>mv mysecondapp apps/<br></td></tr></tbody></table>

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>## important<br>Warning: Don't be tempted to call python manage.py ./apps/mysecondapp. For some reason this deletes all other apps in that directory. I just lost a day of work this way.<br></td></tr></tbody></table>

       * Next, you will need to fix a few imports. Your settings.py should be prefixed with apps:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INSTALLED_APPS = (<br>    ...<br>    'apps.myfirstapp',<br>    'apps.mysecondapp'<br>)<br></td></tr></tbody></table>

       * Lastly, fix your project's urls.py to prefix apps:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>urlpatterns = patterns('', <br>  url(r'^myfirstapp', include('apps.myfirstapp.urls')),<br>  ...<br>)<br></td></tr></tbody></table>

       * Depending on how you wrote them, you might also have to fix a few imports inside your app. Either just use from models import MyFirstModel or also prefix it using from apps.myfirstapp.models import MyFirstModel.

       * In short, if you make your apps directory a python package (by adding \_\_init\_\_.py), you can use it as part of the import path. This should work regardless of the deployment method with no extra configuration.

 * ## Using fixtures when apps are in subdirectories:

     * // Even though we have polls app in a subdirectory while mentioning models 

     * // name we have to mention model name as polls and not polls\_example\_for\_webpack\_and\_reactjs.polls

     * // then we will get the error

     * //    app\_label, model\_name = app\_label.split('.')

     * // ValueError: too many values to unpack (expected 2)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>THIS IS RIGHT<br><br>[<br>  {<br>    "model": "polls.Question",<br>    "pk": 1,<br>    "fields": {<br>      "question_text": "What's new?",<br>      "pub_date": "2019-12-30 18:55:45.597537+05:30"<br>    }<br>  }<br>]<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>THIS IS WRONG<br><br>[<br>  {<br>    "model": "polls_example_for_webpack_and_reactjs.polls.Question",<br>    "pk": 1,<br>    "fields": {<br>      "question_text": "What's new?",<br>      "pub_date": "2019-12-30 18:55:45.597537+05:30"<br>    }<br>  }<br>]<br></td></tr></tbody></table>

     * ### \[images\] [https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error](https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&sa=D&ust=1585972459551000)

       * ![](images/image23.png)![](images/image138.png)![](images/image269.png)![](images/image268.png)

     * ### \[images\] how to tackle with testing error when using subfolders https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder

       * ![](images/image286.png)![](images/image203.png)![](images/image326.png)![](images/image221.png)![](images/image25.png)

 * ## To list the untracked files in the stash:

     * git ls-tree -r stash@{0}^3 --name-only

     * To show a complete diff of all untracked files (with content):

     * git stash show untracked files

     * $ git show stash@{0}^3

     * To show a complete diff of all untracked files (with content):

     * git show stash@{0}^3

     * The reason this works is that git stash creates a merge commit for each stash, which can be referenced as stash@{0}, stash@{1} etc. The first parent of this commit is the HEAD at the time of the stash, the second parent contains the changes to tracked files, and the third (which may not exist) the changes to untracked files.

 * ## “Git stash apply” all files, except one

     * Your best bet is to probably to git stash apply then git checkout -- \[file\] to remove the changes applied when applying the stash.

     * If you have changes in the file already, your best bet is to commit them before applying the stash, you could then rebase the commit and the stash into a single commit later if you wished.

 * ## Tree: how to exclude certain folderr and paths

     * Directly there is no way, but indirectly one can try

     * ### \[code\]

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 19:36:00  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✹ ✭<br>$ tree --noreport --fromfile &lt;&lt;EOF<br>`tree -f -i -n -F --noreport /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/polls_example_for_webpack_and_reactjs | grep -E -v 'templates/.+|migrations/.+|fixtures/.+|^\.$'`<br>EOF<br><br>home<br>└── web_dev<br>    └── DO_NOT_DELETE_djang_basic_documentation_part2<br>        └── basic_django<br>            └── polls_example_for_webpack_and_reactjs<br>                ├── __init__.py<br>                ├── hare.py<br>                ├── models.py<br>                └── polls<br>                    ├── __init__.py<br>                    ├── admin.py<br>                    ├── apps.py<br>                    ├── fixtures<br>                    ├── migrations<br>                    ├── models.py<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br>                    ├── templates<br>                    ├── tests.py<br>                    ├── urls.py<br>                    └── views.py<br><br> 19:36:39  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✹ ✭<br>$ <br></td></tr></tbody></table>

     * ### \[images\] we want to avoid files from templates/fixtures/migrations not to be shown

       * ![](images/image297.png)![](images/image185.png)

 * ## JWT TOKEN:

     * [https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332](https://www.google.com/url?q=https://medium.com/python-pandemonium/json-web-token-based-authentication-in-django-b6dcfa42a332&sa=D&ust=1585972459561000)

     * ![](images/image116.jpg)

     * ### JWT’s Structure:

       * JSON Web Token comprises 3 strings separated by “.” as follows where each part is encoded with base64url encoding :

       * “eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjp7ImlkIjoiNTlhZDFmZTI0MDVkNzk0YTFkYWQ2YmFkIiwiZGlzcGxheV9uYW1lIjoiQWRtaW4iLCJyb2xlX3R5cGUiOiJhZG1pbiJ9LCJpZCI6IlwiNTliYmJjODc0MDVkNzk0NjYwNGEzZjUyXCIiLCJlbWFpbCI6Imp5b3RpZ2F1dGFtMTA4QGdtYWlsLmNvbSJ9.oGA-goFi7ee6DdKn0Z4sctomaY6Ki0mfuJfxT4OK9WA”

       * ![](images/image87.jpg)

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>JWT in short is :- encoded(header)+encoded(payload)+signature(that is already encoded)<br><br>var encoded_string = base64URLEncode(header)+”.”+base64URLEncode(payload)<br>Signature = HMACSHA256(encoded_string,”SECRET”)<br></td></tr></tbody></table>

       * ![](images/image234.png)

       * ![](images/image52.png)

     * ### Creating JSON Web token in python :-

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>First we have to install Python pyjwt library and then using pyjwt:<br><br>&gt;&gt;&gt; import jwt<br>&gt;&gt;&gt; encoded_token = jwt.encode({‘user_id’: “abc”}, ‘SECRET’, algorithm=’HS256')<br>&gt;&gt;&gt; encoded_token<br>‘eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYWJjIn0.OW6BZboviYgO6Yy_UTj5jloba7WlPwZnKHPYDUyY3MU’<br><br>Decoding the above created token on server:<br><br>&gt;&gt;&gt; jwt.decode(encoded_token, ‘SECRET’, algorithms=[‘HS256’])<br>{’user_id’: ’abc’}<br></td></tr></tbody></table>

       * Eg: User and Passwd

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>            payload = {<br>                'id': user.id,<br>                'email': user.email,<br>            }<br>            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}<br><br>           return HttpResponse(<br>              json.dumps(jwt_token),<br>              status=200,<br>              content_type="application/json"<br>            )<br><br>ELSE<br />       else:<br>            return HttpResponse(<br>              json.dumps({'Error': "Invalid credentials"}),<br>              status=400,<br>              content_type="application/json"<br>            )<br><br></td></tr></tbody></table>

 * ## Headers vs Params

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>From discussion with Rob in chat:<br><br>The criteria is that if it's information about the request or about the client, then the header is appropriate.<br>But if it's the content of the request itself (e.g. what you are requesting from the server, some details that identify the item to be returned, some details to be saved on the web server, etc.), then it's a parameter.<br><br>As an example:<br><br>Parameter<br>Let's say you're requesting an image for a product. The product id may be one parameter. The image size (thumbnail vs full size) might be another parameter. The product id and requested image size are examples of "some detail" (or parameter) being supplied as part of the content of a request.<br><br>Header<br>But things like the request is JSON or x-www-form-urlencoded are not the content of the request, but rather information about the request (esp since that's necessary for web service to know how to parse the body of the request). That's why it's a header.s<br></td></tr></tbody></table>

 * ## What's the difference between the square bracket and dot notations in Python?

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>[] is the index to a container, such as a list or dictionary.<br><br>. is the member of an object and modules. It can be a method, member data, or attribute.<br><br>&gt;&gt;&gt; xs = [1, 7, 3, 4, 5, 4, 3, 4, 1]<br><br>&gt;&gt;&gt; xs.count(4)<br>3<br><br>&gt;&gt;&gt; xs[1]<br>7<br></td></tr></tbody></table>

 * ## POSTMAN content-type

     * ![](images/image161.png)

 * ## Django HTTP headers stores with a prefix HTTP\_

     * [https://docs.djangoproject.com/en/3.0/ref/request-response/\#django.http.HttpRequest.META](https://www.google.com/url?q=https://docs.djangoproject.com/en/3.0/ref/request-response/%23django.http.HttpRequest.META&sa=D&ust=1585972459576000)

     * ### \[images\] HTTP\_ prefix

       * ![](images/image238.png)

       * ![](images/image42.png)![](images/image19.png)

 * ## Bytes vs String Python

     * [https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal](https://www.google.com/url?q=https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal&sa=D&ust=1585972459577000)

     * ### \[images\]

       * ![](images/image143.png)

       * ![](images/image176.png)![](images/image251.png)

 * ## Python Split() : 

     * https://www.geeksforgeeks.org/python-string-split/

     * ### \[images\]

       * ![](images/image247.png)![](images/image231.png)![](images/image168.png)![](images/image162.png)![](images/image227.png)

 * ## Logic of get\_jwt\_value of django-rest-framework-jwt:

     * ### \[images\]

       * ![](images/image196.png)

 * ## How to use django 3.0 ORM in a Jupyter Notebook without triggering the async context check?

     * [https://docs.djangoproject.com/en/3.0/topics/async/](https://www.google.com/url?q=https://docs.djangoproject.com/en/3.0/topics/async/&sa=D&ust=1585972459579000)

     * Django 3.0 is adding asgi / async support and with it a guard around making synchronous requests in an async context. Concurrently, IPython just added top level async/await support, which seems to be running the whole interpreter session inside of a default event loop.

     * Unfortunately the combination of these two great addition means that any django ORM operation in a jupyter notebook causes a SynchronousOnlyOperation exception:

     * SynchronousOnlyOperation: You cannot call this from an async context - use a thread or sync\_to\_async.

     * Solution: Change the file /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/.venv/lib/python3.7/site-packages/django/utils/asyncio.py  as per

     * [https://github.com/michalwols/django/commit/b6c2d53a05d0ff720a4bc13cccb2a81571ce6078](https://www.google.com/url?q=https://github.com/michalwols/django/commit/b6c2d53a05d0ff720a4bc13cccb2a81571ce6078&sa=D&ust=1585972459580000)

     * FINAL file code

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>import asyncio<br>import functools<br><br>from django.conf import settings<br>from django.core.exceptions import SynchronousOnlyOperation<br><br><br>def async_unsafe(message):<br>    """<br>    Decorator to mark functions as async-unsafe. Someone trying to access<br>    the function while in an async context will get an error message.<br>    """<br>    def decorator(func):<br>        @functools.wraps(func)<br>        def inner(*args, **kwargs):<br>            if not getattr(settings, 'ALLOW_ASYNC_UNSAFE', False):<br>                # Detect a running event loop in this thread.<br>                try:<br>                    event_loop = asyncio.get_event_loop()<br>                except RuntimeError:<br>                    pass<br>                else:<br>                    if event_loop.is_running():<br>                        raise SynchronousOnlyOperation(message)<br>            # Pass onwards.<br>            return func(*args, **kwargs)<br>        return inner<br>    # If the message is actually a function, then be a no-arguments decorator.<br>    if callable(message):<br>        func = message<br>        message = 'You cannot call this from an async context - use a thread or sync_to_async.'<br>        return decorator(func)<br>    else:<br>        return decorator<br></td></tr></tbody></table>

 * ## Django request logging:

     * [https://stackoverflow.com/a/32017362/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/32017362/2897115&sa=D&ust=1585972459588000)

     * ![](images/image78.png)

     * [https://github.com/Rhumbix/django-request-logging](https://www.google.com/url?q=https://github.com/Rhumbix/django-request-logging&sa=D&ust=1585972459589000)

     * ![](images/image232.png)

 * ## If you can decode JWT how are they secure?

     * [https://stackoverflow.com/questions/27301557/if-you-can-decode-jwt-how-are-they-secure](https://www.google.com/url?q=https://stackoverflow.com/questions/27301557/if-you-can-decode-jwt-how-are-they-secure&sa=D&ust=1585972459589000)

     * ![](images/image295.png)![](images/image8.png)![](images/image120.png)

 * ## Encrypt and decrypt in Django - Ans: better is database

     * [https://stackoverflow.com/questions/51123631/encrypt-and-decrypt-in-django](https://www.google.com/url?q=https://stackoverflow.com/questions/51123631/encrypt-and-decrypt-in-django&sa=D&ust=1585972459590000)

     * ![](images/image89.png)![](images/image128.png)![](images/image204.png)![](images/image313.png)![](images/image10.png)

 * ## How to do hashing more securely - streched hashing

     * [https://stackoverflow.com/questions/4948322/fundamental-difference-between-hashing-and-encryption-algorithms](https://www.google.com/url?q=https://stackoverflow.com/questions/4948322/fundamental-difference-between-hashing-and-encryption-algorithms&sa=D&ust=1585972459591000)

     * ![](images/image83.png)![](images/image349.png)![](images/image126.png)![](images/image244.png)![](images/image317.png)![](images/image256.png)

 * ## Hashing: always use different salt for hash:

     * [https://inspiredelearning.com/blog/the-linkedin-hack-understanding-why-it-was-so-easy-to-crack-the-passwords-2/](https://www.google.com/url?q=https://inspiredelearning.com/blog/the-linkedin-hack-understanding-why-it-was-so-easy-to-crack-the-passwords-2/&sa=D&ust=1585972459592000)

 * ## Attacker sniffs and knows all the api end points and makes better app

     * [https://medium.com/elements/api-request-signing-in-django-bc9389201871](https://www.google.com/url?q=https://medium.com/elements/api-request-signing-in-django-bc9389201871&sa=D&ust=1585972459592000)

 * ## Hmac how it works and two main merits:

     * [https://dev.to/pim/hmac-authentication-better-protection-for-your-api-4e0](https://www.google.com/url?q=https://dev.to/pim/hmac-authentication-better-protection-for-your-api-4e0&sa=D&ust=1585972459593000)

     * The powerful thing about using an HMAC digest in this way, is that it only grants the user access to the specific resource at the URI, /username/securedata in this case. What's more, additional information, most notably a timestamp, can be included which creates "decaying" digests. Meaning if someone obtains the token, they can only request a singular resource and for a limited time. Two big wins from a security point of view.

 * ## JWT why payload is not encrpted - Reason: the cost (however small it is) exceeds the benefit,

     * [https://softwareengineering.stackexchange.com/questions/280257/json-web-token-why-is-the-payload-public](https://www.google.com/url?q=https://softwareengineering.stackexchange.com/questions/280257/json-web-token-why-is-the-payload-public&sa=D&ust=1585972459594000)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>You choose not to encrypt the payload for the same reasons that you choose not to encrypt anything else: the cost (however small it is) exceeds the benefit, and a lot of data simply doesn't need to be secured that way.<br>What you mostly need protection against is people tampering with the data so that the wrong record gets updated, or someone's checking account gets money in it that it's not supposed to have. The JSON Web Token's signature accomplishes that, because changing any part of the header/payload/signature combination invalidates the packet.<br>Note that you can still secure the packets at the Transport Layer by using SSL.<br></td></tr></tbody></table>

 * ## JSON web token - password in the payload? ++ DONT DO IT

     * [https://stackoverflow.com/questions/51035946/json-web-token-password-in-the-payload](https://www.google.com/url?q=https://stackoverflow.com/questions/51035946/json-web-token-password-in-the-payload&sa=D&ust=1585972459595000)

 * ## HMAC  is symmetric whereas assymetric takes more computing

     * [https://security.stackexchange.com/questions/34891/why-a-symmetric-key-for-hmac](https://www.google.com/url?q=https://security.stackexchange.com/questions/34891/why-a-symmetric-key-for-hmac&sa=D&ust=1585972459596000)

     * ![](images/image333.png)

 * ## How does HOTP keep in sync?

     * ![](images/image208.png)![](images/image60.png)

     * ![](images/image199.png)

 * ## Bits and Bytes and characters and how computer stores

     * A computer cannot store "letters", "numbers", "pictures" or anything else. The only thing it can store and work with are bits. A bit can only have two values: yes or no, true or false, 1 or 0 or whatever else you want to call these two values.

     * Since a computer works with electricity, an "actual" bit is a blip of electricity that either is or isn't there. For humans, this is usually represented using 1 and 0 and I'll stick with this convention throughout this article.

     * To use bits to represent anything at all besides bits, we need rules. We need to convert a sequence of bits into something like letters, numbers and pictures using an encoding scheme, or encoding for short. Like this:

     * ![](images/image50.png)

     * ![](images/image309.png)

     * ![](images/image27.png)

     * ![](images/image190.png)

     * ![](images/image259.png)

     * A byte is represents 8 bits binary (0 or 1) data 0  - 255

 * ## How HEX is stored

     * ![](images/image225.png)

     * 4 bits is used to store one value of HEX (0 - F (15) ) - base 16

     * 0 = 0000 (base 2 or binary representation)

     * F = 1111 (1 + 2 + 4+ 8 = 15)

     * Eg 0xF7D = 1111(F=15) 0111(7) 1101(D=13)  = 3965 decimal (base 10)

     * ![](images/image131.png)

     * ![](images/image237.png)

 * ## (Python) view bytes in binary

     * ![](images/image322.png)

     * Answer:

     * ![](images/image301.png)

 * ## Code points to bytes using encoding

     * ![](images/image99.png)

 * ## What is unicode and what is UTF-8 etc

     * ![](images/image287.png)

 * ## (python) Bytes are encoded bytes not code poitns

     * ![](images/image93.png)

 * ## (python) \*\* While encoding using UTF-8 into bytes code points which are greater than FF are encoded (i.e mapped) as combination of multiple ascii extended codepoints

     * HEX = U+0145  \~ Ņ  \~ 325   When encoded using UTF-8 into bytes its not represented as \\x145 rather \\xc5\\x85 i.e in unicode \\xc5 - Å and \\x85

     * ![](images/image14.png)

     * ![](images/image135.png)

 * ## (python) Difference between chr() and bytes.decode

     * ![](images/image302.png)

     * ![](images/image85.png)

     * The chr() method returns the character whose Unicode point is num, an integer.

     * The range may vary from 0 to 1,1141,111(0x10FFFF in base 16).

     * ![](images/image198.png)

 * ## Urandom: os.urandom() generates operating-system-dependent random bytes that can safely be called cryptographically secure:

     * os.urandom() returns a sequence of single bytes:

     * ![](images/image341.png)![](images/image145.png)![](images/image226.png)

     * Urandom(int) will generate a random byte string

     * Then each byte is converted to a string of hex value

     * So we get a double string

     * [https://realpython.com/python-random/\#osurandom-about-as-random-as-it-gets](https://www.google.com/url?q=https://realpython.com/python-random/%23osurandom-about-as-random-as-it-gets&sa=D&ust=1585972459605000)

     * What you’ve mainly dissected here is how a bytes object becomes a Python str. One other technicality is how bytes produced by os.urandom() get converted to a float in the interval \[0.0, 1.0), as in the cryptographically secure version

     * And using force\_text conver to string

     * ![](images/image67.png)

     * datetime.now() and utcnow() are TZ-unaware (that is, the default tzinfo is None). 

     * Naive datetime instances are assumed to represent local time

     * Timestamp

     * It's pretty common to store date and time as a timestamp in a database. A Unix timestamp is the number of seconds between a particular date and January 1, 1970 at UTC.

 * ## timetuple()

     * The timetuple() method of datetime.date instances returns an object of type time.struct\_time. The struct\_time is a named tuple object (A named tuple object has attributes that can be accessed by an index or by name).

     * The struct\_time object has attributes for representing both date and time fields along with a flag to indicate whether Daylight Saving Time is active.

     * ![](images/image284.png)

     * ![](images/image311.png)

 * ## time.mktime() to convert to seconds from epoch

     * time.mktime() method of Time module is used to convert a time.struct\_time object or a tuple containing 9 elements corresponding to time.struct\_time object to time in seconds passed since epoch in local time.

     * ![](images/image272.png)

 * ## HMAC implementation in python

     * ![](images/image336.png)

     * ![](images/image122.png)

     *  HMAC(key, msg, digest).digest() 

     * ![](images/image96.png)

     * In the below using hashlib.sha256

     * ![](images/image192.png)

 * ## pyOTP - TOTP  How to change interval

     * ![](images/image142.png)

     * Solution is Use interval (it kawrgs)

     * ![](images/image354.png)

 * ## Hash Function - Collision resistance

     * ![](images/image180.png)

 * ## What is the difference between a HMAC and a hash of data?

     * ![](images/image20.png)

 * ## Is it possible to reverse a sha1?

     * No, you cannot reverse SHA-1, that is exactly why it is called a Secure Hash Algorithm.

     * SHA-1 is a[ ](https://www.google.com/url?q=http://en.wikipedia.org/wiki/Hash_function&sa=D&ust=1585972459612000)[hash function](https://www.google.com/url?q=http://en.wikipedia.org/wiki/Hash_function&sa=D&ust=1585972459612000) that was designed to make it impractically difficult to reverse the operation. Such hash functions are often called[ ](https://www.google.com/url?q=http://en.wikipedia.org/wiki/One-way_function&sa=D&ust=1585972459612000)[one-way functions](https://www.google.com/url?q=http://en.wikipedia.org/wiki/One-way_function&sa=D&ust=1585972459612000) or[ ](https://www.google.com/url?q=http://en.wikipedia.org/wiki/Cryptographic_hash_function&sa=D&ust=1585972459613000)[cryptographic hash functions](https://www.google.com/url?q=http://en.wikipedia.org/wiki/Cryptographic_hash_function&sa=D&ust=1585972459613000) for this reason.

     * ![](images/image222.png)

     * ![](images/image163.png)

     * ![](images/image140.png)

 * ## What is hashing

     * ![](images/image296.png)

 * ##  How to hack a hash

     * ![](images/image16.png)

     * ![](images/image325.png)

 * ## HMAC vs salted hash

     * HMAC is basically hashing data with a secret (aka a salt), with one or more tweaks to make it exceptionally hard for someone to recompute the hash...

 * ## HMAC vs salted hash for password

     * ![](images/image147.png)

     * ANSWER

     * ![](images/image171.png)

 * ## What is the difference between hash salting and noncing?

     * ![](images/image86.png)

 * ## (Python) for loop in range

     * ![](images/image315.png)

 * ## (python) Get random string in python:

     * ![](images/image158.png)

     * ![](images/image44.png)

 * ## Django: How will django protect from knowing the passwords by using hashes if someone have access to the database  

     * Why Django Uses random hash and store it along with password

     * ![](images/image157.png)

     * Answer:

     * ![](images/image183.png)

 * ## Difference between Hashing a Password and Encrypting it

     * ![](images/image90.png)

 * ## Difference between salted hash and keyed hashing?

     * Salts  are intended to deter brute-force attacks, they are intentionally designed to be slow. Also, as you said, salts are not assumed to be secret.

     * You can build a salted hash out of a MAC by using[ ](https://www.google.com/url?q=http://en.wikipedia.org/wiki/PBKDF2&sa=D&ust=1585972459619000)[PBKDF2](https://www.google.com/url?q=http://en.wikipedia.org/wiki/PBKDF2&sa=D&ust=1585972459619000), which basically applies the MAC a lot of times (to make it slower).

     * The main difference is that the salt is not assumed unknown to the attacker, but the key is. An additional difference is that salts are supposed to vary; if you hash three passwords within the same system, then you should use three distinct salt values, whereas keys are reused.

     * ![](images/image5.png)

 * ## What key is used for hmac in PBKDF2

     * ![](images/image294.png)

     * ![](images/image40.png)

 * ## Reply ATTACK - Solution using  Nonce to keep a message unique from all other messages

     * https://books.google.co.in/books?id=NUWyDwAAQBAJ\&pg=PA211\&lpg=PA211\&dq=you+may+need+a+nonce+or+IV+value\&source=bl\&ots=ox0zLbptUa\&sig=ACfU3U2oi8IoElPKNyC1MIfr34Km5pXumA\&hl=en\&sa=X\&ved=2ahUKEwifivnhhrznAhWc7HMBHSnrCccQ6AEwDnoECAgQAQ\#v=onepage\&q\&f=false

     * ![](images/image327.png)

 * ## 

 * ## TOTP Base32 vs Base64

     * ![](images/image62.png)![](images/image55.png)![](images/image111.png)![](images/image121.png)

 * ## [https://cryptii.com/pipes/hex-to-base32](https://www.google.com/url?q=https://cryptii.com/pipes/hex-to-base32&sa=D&ust=1585972459621000)

     * Useful to check different

     * ![](images/image292.png)

 * ## Hexadecimal

     * ![](images/image348.png)

 * ## Convert binary to Hex

     * [https://www.sciencedirect.com/topics/engineering/hexadecimal](https://www.google.com/url?q=https://www.sciencedirect.com/topics/engineering/hexadecimal&sa=D&ust=1585972459622000)

     * ![](images/image280.png)

     * ![](images/image47.png)

     * ![](images/image240.png)

     * ![](images/image263.png)

 * ## (python) How to create secret key i.e base32-formatted

     * Ans:

     * base64.b32encode("secret")

     * https://github.com/pyauth/pyotp/issues/43

     * ![](images/image342.png)

 * ## (python - nonce) What is the standard method for generating a nonce in Python?

     * [https://stackoverflow.com/questions/5590170/what-is-the-standard-method-for-generating-a-nonce-in-python](https://www.google.com/url?q=https://stackoverflow.com/questions/5590170/what-is-the-standard-method-for-generating-a-nonce-in-python&sa=D&ust=1585972459625000)

     * ![](images/image206.png)

 * ## (python - secret token) The New Way To Generate Secure Tokens in Python

     * [https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python](https://www.google.com/url?q=https://blog.miguelgrinberg.com/post/the-new-way-to-generate-secure-tokens-in-python&sa=D&ust=1585972459626000)

     * ![](images/image274.png)

 * ## (python - secure random) Cryptographically Secure Random Data in Python

     * [https://realpython.com/lessons/cryptographically-secure-random-data-python/](https://www.google.com/url?q=https://realpython.com/lessons/cryptographically-secure-random-data-python/&sa=D&ust=1585972459626000)

     * ![](images/image76.png)![](images/image266.png)![](images/image166.png)![](images/image112.png)![](images/image235.png)![](images/image330.png)![](images/image124.png)![](images/image41.png)![](images/image265.png)![](images/image97.png)

 * ## (python - nonce) Another way to generate nonce in python

     * ![](images/image270.png)

 * ## What is the difference between a digest and a hash function?

     * ![](images/image254.png)

 * ## What is hash

     * ![](images/image334.png)![](images/image144.png)

 * ##  Base64 encoding vs Base64url encoding 

     * [http://websecurityinfo.blogspot.com/2017/06/base64-encoding-vs-base64url-encoding.html](https://www.google.com/url?q=http://websecurityinfo.blogspot.com/2017/06/base64-encoding-vs-base64url-encoding.html&sa=D&ust=1585972459629000)

     * ![](images/image92.png)![](images/image339.png)![](images/image118.png)

 * ## Difference between ASCII and UNICODE ?

     * ![](images/image77.png)

 * ## Ascii 7-bit

     * 01111111 = 127 

     * Where as

     * An 8-bit byte can represent a number between 0 and 255. Or, a number between -128 and +127. Similarly, a 2-byte word can represent a number between 0 and 65535... or between -32768 and +32767.

 * ## ASCII table

     * http://www.asciitable.com/

     * ![](images/image260.png)

 * ## ASCII Converter - Hex, decimal, binary, base64, and ASCII converter

     * [https://www.branah.com/ascii-converter](https://www.google.com/url?q=https://www.branah.com/ascii-converter&sa=D&ust=1585972459631000)

 * ## How Text strings are stored in computer

     * Each ASCII character is stored is stored as one byte

     * Eg: hello world\! (12 characters stored as 12 bytes)

     * ![](images/image285.png)

 * ## (Python) how strings are stored

     * ![](images/image331.png)

     * ![](images/image68.png)

 * ## (Python) convert a integer to unicode character

     * ![](images/image29.png)

     * ![](images/image169.png)

 * ## (python/unicode) U+ u’ \\u2 (unicode code points representation)

     * ![](images/image310.png)

 * ## Unicode Code point:

     * http://unicode.org/glossary/\#code\_point

     * ![](images/image248.png)

     * A Python unicode object is a series of Unicode code points. There are 1,112,064 valid code points in the Unicode code space. 

 * ## (Python) byte literal (b preix) and plain string 

     * ![](images/image258.png)

     * Python bytes and escape literals

     * ![](images/image103.png)![](images/image271.png)

     * Numeric value greater than 128 are expresses with escapes

     * But there are various groups inbetween 0-127. So non printable characters expressed as escape sequence

     * ![](images/image154.png)

 * ## (python) Bytes object

     * ![](images/image277.png)

     * ![](images/image109.png)

     * ### Explaining the rules for bytes object and ascii characters

       * Bytes object is a sequence of integers in the range 0-255. 

       * ![](images/image151.png)

       * Here b’A’ == b’\\x41’

       * \\x41 in ASCII table represents A

       * ![](images/image242.png)

       * Any ASCII priting character is also allowed to be represented as it is instead of hex representation. Where as non printing characters have to be represented as hex

 * ## Encode to str to byte and decode byte to str

     * ![](images/image351.png)

 * ## Unicode is not encoding:

     * So, how many bits does Unicode use to encode all these characters? None. Because Unicode is not an encoding.

     *  Unicode first and foremost defines a table of code points for characters. That's a fancy way of saying "65 stands for A, 66 stands for B and 9,731 stands for ☃" (seriously, it does).

     * To represent 1,114,112 different values, two bytes aren't enough. Three bytes are, but three bytes are often awkward to work with, so four bytes would be the comfortable minimum.

     *  If the letter "A" was always encoded to 00000000 00000000 00000000 01000001, "B" always to 00000000 00000000 00000000 01000010 and so on, any document would bloat to four times the necessary size.

 * ## Code Point

     * ![](images/image15.png)

 * ## UTF 32 vs UTF-16 vs UTF - 8

     * To represent 1,114,112 different values, two bytes aren't enough. Three bytes are, but three bytes are often awkward to work with, so four bytes would be the comfortable minimum.

     *  If the letter "A" was always encoded to 00000000 00000000 00000000 01000001, "B" always to 00000000 00000000 00000000 01000010 and so on, any document would bloat to four times the necessary size.

     * ![](images/image17.png)

     * ![](images/image217.png)

 * ## (Python) Testing unicode, byte and encoding:

     * ![](images/image132.png)![](images/image48.png)![](images/image146.png)![](images/image139.png)

 * ## Symmetric vs asymetric keys

     * ![](images/image21.png)

     * ![](images/image6.png)

     * ![](images/image197.png)

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>def get_random_secret_key():<br>    """<br>    Return a 50 character random string usable as a SECRET_KEY setting value.<br>    """<br>    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&amp;*(-_=+)'<br>    return get_random_string(50, chars)<br><br><br>def get_random_string(length=12,<br>                      allowed_chars='abcdefghijklmnopqrstuvwxyz'<br>                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):<br>    """<br>    Return a securely generated random string.<br><br>    The default length of 12 with the a-z, A-Z, 0-9 character set returns<br>    a 71-bit value. log_2((26+26+10)^12) =~ 71 bits<br>    """<br>    return ''.join(secrets.choice(allowed_chars) for i in range(length))<br><br><br><br></td></tr></tbody></table>

     * ![](images/image352.png)

 * ## (python) Django Random secret i.e secrets.choice vs secrets.token\_urlsafe

     * ![](images/image267.png)

 * ## (python) Saving utf-8 texts in json.dumps as UTF8, not as \\u escape sequence

     * https://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence

     * ![](images/image63.png)

     * SOLUTION: Use the ensure\_ascii=False switch to json.dumps()

     * ![](images/image30.png)

 * ## (Python) String literals truncated \\UXXXXXXXX escape

     * ![](images/image54.png)

     * Solution is to add r’’ or escape the backslash. Because in python backslash acts as escape.

     * ![](images/image94.png)

     * ![](images/image343.png)

 * ## (jupyter) Adding word wrap to jupyter

     * ![](images/image170.png)

 * ## (jupyter) Bringing the scrol bar to main page in jupyter

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>~/.jupyter/custom/custom.css<br><br>#site{<br>        overflow: unset<br>}<br><br>Also we have to toggle the scrollbar to sometimes for convinience so we use a javascript bookmarklet<br><br>Tg_nb:<br><br>javascript:(function(){if(document.getElementById("site").style.overflow=="auto"){document.getElementById("site").style.overflow="";} else{document.getElementById("site").style.overflow="auto";};})();<br></td></tr></tbody></table>

     * ### Problem:

       * https://stackoverflow.com/questions/60528336/jupyter-notebook-does-not-page-scroll-when-using-firefoxs-take-a-screenshot-p

       * ![](images/image110.png)

 * ## (Python) raw text and escapes

     * ![](images/image236.png)

     * -----

 * ## Website Unicode Code Character, character, utf-8, Decomposition, Lowercase Character:

     * [https://www.compart.com/en/unicode/U+015A](https://www.google.com/url?q=https://www.compart.com/en/unicode/U%2B015A&sa=D&ust=1585972459649000)

     * Best place to know about unicode characters and all the required information at one place

     * Eg: [https://www.compart.com/en/unicode/U+015A](https://www.google.com/url?q=https://www.compart.com/en/unicode/U%2B015A&sa=D&ust=1585972459650000)

     * ![](images/image308.png)![](images/image2.png)![](images/image219.png)![](images/image323.png)

 * ## Unicode character dotted circle used for displaying diacratics etc while combination characters

     * ![](images/image107.png)![](images/image182.png)

 * ## (Python) Unicode combination characters example

     * ![](images/image35.png)

 * ## unicode: find out the corresponding single unicode for a character formed by combination of unicodes \[duplicate\]: (Normalizing Unicode)

     * Q: 

     * ![](images/image155.png)

     * Answer:

     * ![](images/image153.png)

     * Answer:

     * ![](images/image290.png)

 * ## Unicode characters Non combined to Combined and back

     * ![](images/image299.png)![](images/image173.png)![](images/image64.png)

 * ## Byte to Bytearray and reverse

     * ![](images/image43.png)

 * ## Firefox remove headers

     * |                                                                                                                                                                                                                                                                                                                                                              |

     * | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

     * | javascript:(function(){var%20found=true;while(found){var%20elems=document.body.getElementsByTagName("\*");var%20len=elems.length;for(var%20i=0;i\<len;i++){found=false;if(window.getComputedStyle(elems\[i\],null).getPropertyValue('position')=='fixed'){var%20el=elems\[i\];el.parentNode.removeChild(el);found=true;break;}}}})() |

     * ![](images/image113.png)

 * ## (python) PyOTP secret cannot be a non base32 type

     * ![](images/image338.png)

 * ## How to convert a string to base32 string and back

     * ![](images/image149.png)

 * ## Python replace

     * ![](images/image59.png)

 * ## Sublime text navigating python code

     * To navigate python code (best way, it shows previous and next)

     * { "keys": \["alt+up"\], "command": "jump\_prev\_indent" },

     * { "keys": \["alt+shift+up"\], "command": "jump\_prev\_indent", "args": { "extend\_selection": true} },

     * { "keys": \["alt+down"\], "command": "jump\_next\_indent" },

     * { "keys": \["alt+shift+down"\], "command": "jump\_next\_indent", "args": { "extend\_selection": true} }

     * To select python code (start and end type)

     * { "keys": \["ctrl+alt+e"\], "command": "open\_dir", 

     * "args": {"dir": "$file\_path", "file": "$file\_name"} },

     * { "keys": \["super+shift+space"\], "command": "expand\_region" },

     * {

     *   "keys": \["super+u"\],

     *   "command": "expand\_region",

     *   "args": {"undo": true},

     *   "context": \[{ "key": "expand\_region\_soft\_undo" }\]

     * },

     * Expand selection to indentation (from sublime text)

     * { "keys": \["ctrl+shift+j"\], "command": "expand\_selection", "args": {"to": "indentation"} },

 * ## How to present the code for documentation:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Add <br><br>(should have a new line above and also below ? ###)<br><br># ???<br>some code<br># ???(not spaces here)<br><br>(should have a new line below)<br><br><br>Copy the code to new file<br><br>NOw select using the below reg ex:<br><br>(?s)\n *# \?\?\?(?:(?!# \?\?\?).)*(?!&gt;# \?\?\?\n)<br><br>Then invert selection<br><br>Ctrl + shift + {  ( to hide)<br><br>Or delete the code and ctrl + alt  + n (to convert to html) and then ctrl + alt  + v to open in browser<br><br><br></td></tr></tbody></table>

     * ![](images/image56.png)

     * To 

     * ![](images/image253.png)

