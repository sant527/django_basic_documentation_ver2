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
   * [<span>Miscellaneous</span>](#miscellaneous)
      * [<span>Webpack Main Concepts</span>](#webpack-main-concepts)
         * [<span>Entry</span>](#entry)
         * [<span>Output</span>](#output)
         * [<span>Loaders</span>](#loaders)
         * [<span>Plugins</span>](#plugins)
         * [<span>Mode</span>](#mode)
      * [<span>Webpack: how to have multiple entries and outputs and easily use them in template</span>](#webpack-how-to-have-multiple-entries-and-outputs-and-easily-use-them-in-template)
         * [<span>[code] settings.py</span>](#code-settingspy)
         * [<span>[code] Webpack.config.js:</span>](#code-webpackconfigjs-1)
         * [<span>[image] webpack.config.js</span>](#image-webpackconfigjs)
         * [<span>[code] templates/polls/index.html</span>](#code-templatespollsindexhtml)
         * [<span>[code] polls/urls.py</span>](#code-pollsurlspy)
         * [<span>[code] polls/views,py</span>](#code-pollsviewspy)
         * [<span>[code] polls/static/polls/js/index.js</span>](#code-pollsstaticpollsjsindexjs)
      * [<span>How to integrate Django API project with nodejs and react on frontend?. Why not to use SPA</span>](#how-to-integrate-django-api-project-with-nodejs-and-react-on-frontend-why-not-to-use-spa)
      * [<span>Webpack: Multiple entry points:</span>](#webpack-multiple-entry-points)
      * [<span>Webpack: path as the entry name: How to set multiple file entry and output in project with webpack?</span>](#webpack-path-as-the-entry-name-how-to-set-multiple-file-entry-and-output-in-project-with-webpack)
      * [<span>Webpack: multiple output paths</span>](#webpack-multiple-output-paths)
      * [<span>Django-webpack-loader: </span><span><a href="https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&amp;sa=D&amp;ust=1577129044888000" rel="nofollow">https://github.com/owais/django-webpack-loader</a></span>](#django-webpack-loader-httpsgithubcomowaisdjango-webpack-loader)
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
         * [<span>[images] </span><span><a href="https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&amp;sa=D&amp;ust=1577129044948000" rel="nofollow">https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error</a></span>](#images-httpsstackoverflowcomquestions10313475moving-django-apps-into-subfolder-and-url-py-error)
         * [<span>[images] how to tackle with testing error when using subfolders <a href="https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder" rel="nofollow">https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder</a></span>](#images-how-to-tackle-with-testing-error-when-using-subfolders-httpsstackoverflowcomquestions6483636how-to-test-django-application-placed-in-subfolder)
      * [<span>To list the untracked files in the stash:</span>](#to-list-the-untracked-files-in-the-stash)
      * [<span>“Git stash apply” all files, except one</span>](#git-stash-apply-all-files-except-one)
      * [<span>Tree: how to exclude certain folderr and paths</span>](#tree-how-to-exclude-certain-folderr-and-paths)
         * [<span>[code]</span>](#code)
         * [<span>[images] we want to avoid files from templates/fixtures/migrations not to be shown</span>](#images-we-want-to-avoid-files-from-templatesfixturesmigrations-not-to-be-shown)
* # Create folder DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ cd /home/web_dev<br>$ mkdir DO_NOT_DELETE_djang_basic_documentation_part2<br></td></tr></tbody></table>

* # Create a new repoitory in github

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Go to<br><a href="https://www.google.com/url?q=https://github.com/new&amp;sa=D&amp;ust=1577129044592000" class="c16">https://github.com/new</a><br><br>Then add a name: django_basic_documentation_ver2<br><br>Dont select README<br><br>The new url of the github project is<br><br><a href="https://www.google.com/url?q=https://github.com/sant527/django_basic_documentation_ver2&amp;sa=D&amp;ust=1577129044593000" class="c16">https://github.com/sant527/django_basic_documentation_ver2</a><br></td></tr></tbody></table>

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

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The github url is:<br><a href="https://www.google.com/url?q=https://github.com/sant527/django_basic_documentation&amp;sa=D&amp;ust=1577129044604000" class="c16">https://github.com/sant527/django_basic_documentation</a><br><br>Now we want to get the basic_django from the last or 13th commit<br><br>We will use svn to export a particular folder from git<br><br>$ svn log https://github.com/sant527/django_basic_documentation<br>------------------------------------------------------------------------<br>r13 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Thirteenth Commit: This is example for Third Commit custom logging and pretty print functions<br><br>------------------------------------------------------------------------<br>r12 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Twelveth Commit: Logging via email and OTP, views,forms, templates<br><br>------------------------------------------------------------------------<br>r11 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Eleventh_A Commit: add articles and login_register_password apps to settings<br><br>------------------------------------------------------------------------<br>r10 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Eleventh Commit: create articles and login_register_password app<br><br>------------------------------------------------------------------------<br>r9 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Ninth Commit:  Added custom model and manager and AUTH_USER_MODEL to settings and migrate<br><br>------------------------------------------------------------------------<br>r8 | santhosh | 2019-10-18 12:02:40 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Sixth_A Commit: Add the app to the settings<br><br>------------------------------------------------------------------------<br>r7 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Sixth Commit: creating an app for custom_user using manage.py startapp<br><br>------------------------------------------------------------------------<br>r6 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>FIFTH COMMIT: Celery and redis<br><br>------------------------------------------------------------------------<br>r5 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>FOURTH COMMIT: creating new gmail account, use 2 step verification, create app password, DJANO email config, view to send email<br><br>------------------------------------------------------------------------<br>r4 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>THIRD COMMIT: pretty print obj, sql, pygment, sqlparse, django-extensions, ipython, jupyter, runserver_plus, werkzeug, graph_models, django-querycount, pudb debugger, logging - start,stop, custom format, filters, traceback<br><br>------------------------------------------------------------------------<br>r3 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Second Commit: django-environ and .env and setttings.py and psycopg2 and sensitive information secure<br><br>------------------------------------------------------------------------<br>r2 | santhosh | 2019-10-18 12:02:39 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>First Commit: Fresh virtualenv with pipenv and install django and remove SECRETKEY<br><br>------------------------------------------------------------------------<br>r1 | santhosh | 2019-10-18 12:02:36 +0530 (Fri, 18 Oct 2019) | 2 lines<br><br>Zero Commit: Documentation Django, git, awk, commands, gitignore<br><br>------------------------------------------------------------------------<br><br>It show r1, r2, r3 etc and the corresponding commit<br><br>From above r13 is the latest revision<br><br>$ svn ls -r13 https://github.com/sant527/django_basic_documentation<br>branches/<br>trunk/<br><br>$ svn ls -r13 https://github.com/sant527/django_basic_documentation/trunk<br>.gitignore<br>DjangoDocumentation_docx_and_htmlzip/<br>Pipfile<br>Pipfile.lock<br>README.md<br>awkdoc/<br>basic_django/<br>commands.txt<br>flowcharts/<br>gitdoc/<br>images/<br><br>## get the basic_django folder<br>$ svn export -r13 https://github.com/sant527/django_basic_documentation/trunk/basic_django<br><br>The above command will export the folder to here<br><br>$ ls -al<br>total 24<br>drwxr-xr-x  4 simha users 4096 Nov 22 23:22 .<br>drwxr-xr-x 39 simha users 4096 Nov 21 18:53 ..<br>drwxr-xr-x  7 simha users 4096 Nov 22 23:22 basic_django<br>drwxr-xr-x  8 simha users 4096 Nov 22 23:24 .git<br>-rw-r--r--  1 simha users 4892 Nov 22 23:18 .gitignore<br><br>$ git status<br>On branch master<br>Untracked files:<br>  (use "git add &lt;file&gt;..." to include in what will be committed)<br><br>        basic_django/<br><br>nothing added to commit but untracked files present (use "git add" to track)<br><br>https://stackoverflow.com/questions/39030116/how-to-see-untracked-files-in-git-instead-of-untracked-directory?rq=1<br>NOTE: If git only shows that the directory is untracked, then every file in it (including files in subdirectories) is untracked.<br><br>If you have some ignored files in the directory, pass the -u flag when running git status (i.e., git status -u) to show the status of individual untracked files.<br><br>$ git status -u<br>On branch master<br>Untracked files:<br>  (use "git add &lt;file&gt;..." to include in what will be committed)<br><br>        basic_django/articles/__init__.py<br>        basic_django/articles/admin.py<br>        basic_django/articles/apps.py<br>        basic_django/articles/migrations/__init__.py<br>        basic_django/articles/models.py<br>        basic_django/articles/templates/articles/base.html<br>        basic_django/articles/templates/articles/main_page/articles.html<br>        basic_django/articles/tests.py<br>        basic_django/articles/urls.py<br>        basic_django/articles/views.py<br>        basic_django/basic_django/.env.example<br>        basic_django/basic_django/__init__.py<br>        basic_django/basic_django/celery.py<br>        basic_django/basic_django/settings.py<br>        basic_django/basic_django/tasks.py<br>        basic_django/basic_django/urls.py<br>        basic_django/basic_django/views.py<br>        basic_django/basic_django/wsgi.py<br>        basic_django/custom_user/__init__.py<br>        basic_django/custom_user/admin.py<br>        basic_django/custom_user/apps.py<br>        basic_django/custom_user/fixtures/ActionTypeForUserSessionLog.json<br>        basic_django/custom_user/migrations/0001_initial.py<br>        basic_django/custom_user/migrations/0002_auto_20191016_0203.py<br>        basic_django/custom_user/migrations/0003_auto_20191017_1002.py<br>        basic_django/custom_user/migrations/__init__.py<br>        basic_django/custom_user/models.py<br>        basic_django/custom_user/tests.py<br>        basic_django/custom_user/views.py<br>        basic_django/login_register_password/__init__.py<br>        basic_django/login_register_password/admin.py<br>        basic_django/login_register_password/apps.py<br>        basic_django/login_register_password/forms.py<br>        basic_django/login_register_password/migrations/__init__.py<br>        basic_django/login_register_password/models.py<br>        basic_django/login_register_password/templates/login_register_password/base.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/email/login_otp_sendemail.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/user_login_via_otp_form_email.html<br>        basic_django/login_register_password/templates/login_register_password/login_via_otp/user_login_via_otp_form_otp.html<br>        basic_django/login_register_password/tests.py<br>        basic_django/login_register_password/urls.py<br>        basic_django/login_register_password/views.py<br>        basic_django/manage.py<br>        basic_django/querycount_mod/__init__.py<br>        basic_django/querycount_mod/middleware.py<br>        basic_django/querycount_mod/middleware_backup.py<br>        basic_django/querycount_mod/qc_settings.py<br><br>nothing added to commit but untracked files present (use "git add" to track)<br><br>$ git add -A<br><br>$ git commit -m 'Base Commit: This is basically the basic_django folder from thirteenth Commit from django_basic_documentation'<br></td></tr></tbody></table>

* # Base Commit 2: Copy Pipfile and Pipfile.lock

 * ## \[code\] Copy pipenv and piplock files and add them to the git

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ svn export https://github.com/sant527/django_basic_documentation/trunk/Pipfile.lock<br><br>$ svn export https://github.com/sant527/django_basic_documentation/trunk/Pipfile<br><br>$ Git add -A<br><br>$ git commit -m 'Base Commit 2: Copy Pipfile and Pipfile.lock'<br></td></tr></tbody></table>

* # Base Commit 3: Setup Virtual env: run pipenv install --dev (empty commit)

 * ## \[code\] install the python virualenv (install dev packages also for development) 

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$ export PIPENV_VENV_IN_PROJECT=1<br><br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$ pipenv shell<br>Creating a virtualenv for this project…<br>Pipfile: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/Pipfile<br>Using /usr/bin/python (3.7.3) to create virtualenv…<br>⠴ Creating virtual environment...Already using interpreter /usr/bin/python<br>Using base prefix '/usr'<br>New python executable in /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/python<br>Installing setuptools, pip, wheel...<br>done.<br><br>✔ Successfully created virtual environment! <br>Virtualenv location: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✔ <br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>## To install dev packages also use<br>⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔ <br>$ pipenv install --dev <br>Installing dependencies from Pipfile.lock (235b42)…<br>  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 65/65 — 00:00:36<br><br></td></tr></tbody></table>

 * ## \[image\] terminator screenshots of the above commands

     * ![](images/image70.png)

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

     * ![](images/image59.png)![](images/image2.png)![](images/image31.png)

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

       * ![](images/image20.png)

 * ## Start celery

     * ### \[code\] starting celery

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> simha  ~<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$ pipenv shell<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✭<br>$ cd basic_django <br><br> simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✭<br>$ celery -A basic_django worker --loglevel=debug #ensure redis-server is running in root<br><br><br><br></td></tr></tbody></table>

     * ### \[image\] staring celery

       * ![](images/image3.png)

       * ![](images/image35.png)

 * ## Start runserver

     * ### \[code\] start runserver

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#### change directory<br> 17:41:03  simha  ~<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>#### start virtual env<br> 17:41:09  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$ pipenv shell<br>Launching subshell in virtual environment…<br> . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br> 17:41:12  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2   master ✘ ✭<br>$  . /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/.venv/bin/activate<br><br>#### change to project directory<br> 17:41:12  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✭<br>$ cd basic_django <br><br>#### start runserver<br> 17:41:17  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✭<br>$ ./manage.py runserver<br>Watching for file changes with StatReloader<br>Performing system checks...<br><br>System check identified no issues (0 silenced).<br>December 02, 2019 - 12:11:22<br>Django version 2.2.6, using settings 'basic_django.settings'<br>Starting development server at http://127.0.0.1:8000/<br>Quit the server with CONTROL-C.<br></td></tr></tbody></table>

     * ### \[image\] start runserver

       * ![](images/image48.png)

 * ## \[code\] Git commit

     * |                                                                                                                        |

     * | ---------------------------------------------------------------------------------------------------------------------- |

     * | git commit --allow-empty -m 'Basic Commit 6: Checking the server: runserver, redis and celery' |

* # First Commit: Add TESTING\_EMAIL2 to settings.py

     * We want to create TESTING\_EMAIL2="<test@xyz.com>" which will be used while showing any examples in github.

 * ## \[code\] edit settings.py and add testing\_email2

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Edit settings.py and add TESTING_EMAIL2<br><br># we want to use this mainly to show in github any example<br>TESTING_EMAIL2="test@xyz.com"<br></td></tr></tbody></table>

 * ## \[image\] add testing\_email2 to settings.py

     * ![](images/image46.png)

 * ## \[image\] commands to get the diff file and change + to +++ and - to ---

     * ![](images/image6.png)

 * ## \[image\] settings.py diff file

     * ![](images/image71.png)

 * ## \[code\] create a commit

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ Git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   basic_django/settings.py<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br>Git add -A<br><br> 19:34:54  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✚<br>$ git commit -m 'First Commit: Add TESTING_EMAIL2 to settings.py'                                     <br>[master fd300e2] First Commit: Add TESTING_EMAIL2 to settings.py<br> 1 file changed, 2 insertions(+)<br><br><br></td></tr></tbody></table>

* # 

* # Second Commit: Add Django remote forms package

     * [https://github.com/WiserTogether/django-remote-forms](https://www.google.com/url?q=https://github.com/WiserTogether/django-remote-forms&sa=D&ust=1577129044663000)

     * A package that allows you to serialize django forms, including fields and widgets into Python dictionary for easy conversion into JSON and expose over API

 * ## \[code\] how to get django\_remote\_forms and commit the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>The github url is:<br><a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1577129044665000" class="c16">https://github.com/sant527/django_remote_forms</a><br><br>Now we want to get the django_remote_forms from the last or latest commit<br><br>We will use svn to export a particular folder from git<br><br>### change into the project folder<br>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django<br><br>### check the folder structure<br>$ tree -L 1 -a<br><br>### get the log of svn<br>$ svn log <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1577129044667000" class="c16">https://github.com/sant527/django_remote_forms</a><br><br>### check the folder <br>$ svn ls -r1 <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms&amp;sa=D&amp;ust=1577129044668000" class="c16">https://github.com/sant527/django_remote_forms</a><br>branches/<br>trunk/<br><br>### check the folder <br>$ svn ls -r1 <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms/trunk&amp;sa=D&amp;ust=1577129044669000" class="c16">https://github.com/sant527/django_remote_forms/trunk</a><br>django_remote_forms/<br><br>### export the folder here<br>$ svn export -r1 https://github.com/sant527/django_remote_forms/trunk/django_remote_forms<br><br>### check the folder structure<br>$ tree -L 1 -a<br><br>### check git status<br>$ git status<br><br>### stage changes<br>$ git add -A<br><br>### commit the changes<br>$ git commit -m "Second Commit: get the django_remote_forms folder from <a href="https://www.google.com/url?q=https://github.com/sant527/django_remote_forms/&amp;sa=D&amp;ust=1577129044672000" class="c16">https://github.com/sant527/django_remote_forms/</a>"<br><br>### check git log<br>$ git --no-pager log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(green)%s%C(reset) %C(dim magenta)- %an%C(reset)' --all<br><br>### git remote check<br>$ git remote -v<br><br>### push to remote<br>$ git push -f origin master<br><br>### check git log<br>$ git --no-pager log --graph --abbrev-commit --decorate --format=format:'%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(auto)%d%C(reset)%n''          %C(green)%s%C(reset) %C(dim magenta)- %an%C(reset)' --all<br></td></tr></tbody></table>

 * ## \[image\] screenshot of terminator for this commit

     * ![](images/image32.png)![](images/image55.png)![](images/image39.png)![](images/image60.png)![](images/image67.png)![](images/image22.png)

 * ## \[code\] Some sample Example

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Minimal Example:<br><br>from django_remote_forms.forms import RemoteForm<br><br>form = LoginForm()<br>remote_form = RemoteForm(form)<br>remote_form_dict = remote_form.as_dict()<br><br>Upon converting the dictionary into JSON, it looks like this:<br><br>{<br>    "is_bound": false,<br>    "non_field_errors": [],<br>    "errors": {},<br>    "title": "LoginForm",<br>    "fields": {<br>        "username": {<br>            "title": "CharField",<br>            "required": true,<br>            "label": "Username",<br>            "initial": null,<br>            "help_text": "This is your django username",<br>            "error_messages": {<br>                "required": "This field is required.",<br>                "invalid": "Enter a valid value."<br>            },<br>            "widget": {<br>                "title": "TextInput",<br>                "is_hidden": false,<br>                "needs_multipart_form": false,<br>                "is_localized": false,<br>                "is_required": true,<br>                "attrs": {<br>                    "maxlength": "30"<br>                },<br>                "input_type": "text"<br>            },<br>            "min_length": 6,<br>            "max_length": 30<br>        },<br>        "password": {<br>            "title": "CharField",<br>            "required": true,<br>            "label": "Password",<br>            "initial": null,<br>            "help_text": "",<br>            "error_messages": {<br>                "required": "This field is required.",<br>                "invalid": "Enter a valid value."<br>            },<br>            "widget": {<br>                "title": "PasswordInput",<br>                "is_hidden": false,<br>                "needs_multipart_form": false,<br>                "is_localized": false,<br>                "is_required": true,<br>                "attrs": {<br>                    "maxlength": "128"<br>                },<br>                "input_type": "password"<br>            },<br>            "min_length": 6,<br>            "max_length": 128<br>        }<br>    },<br>    "label_suffix": ":",<br>    "prefix": null,<br>    "csrfmiddlewaretoken": "2M3MDgfzBmkmBrJ9U0MuYUdy8vgeCCgw",<br>    "data": {<br>        "username": null,<br>        "password": null<br>    }<br>}<br><br></td></tr></tbody></table>

* # Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail

 * ## \[code\] UserLoginViaOtpFormEmail (this already defined)

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/forms.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from custom_user.models import User<br>from django import forms<br>from basic_django import settings<br><br>class UserLoginViaOtpFormEmail(forms.ModelForm):<br>    class Meta:<br>        model = User<br>        fields = ['email']<br><br>    # we can create the email manually, but since its already defined we take advantage from model<br><br>    ############### important whenever for ease we use a field from a model################### <br>    # if we dont call clean. it<br>    #will check for unique instance clause for email  and gives User already exists:<br>    #go to: class BaseModelForm(BaseForm): --- self._validate_unique = False<br>    def clean(self):<br>        return self.cleaned_data<br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image57.png)

 * ## \[code\] api endpoint: api\_user\_login\_via\_otp\_form\_email\_django\_forms\_example

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/views.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.core.serializers.json import DjangoJSONEncoder<br>from django.views.decorators.csrf import csrf_exempt<br>from django.middleware.csrf import CsrfViewMiddleware<br>from django_remote_forms.forms import RemoteForm<br>import json<br>from .forms import UserLoginViaOtpFormEmail<br>from django.http import HttpResponse<br><br><br>@csrf_exempt<br>def api_user_login_via_otp_form_email_django_forms_example(request):<br>    csrf_middleware = CsrfViewMiddleware()<br><br>    response_data = {}<br>    if request.method == 'GET':<br>        # Get form definition<br>        form = UserLoginViaOtpFormEmail(initial={'email': settings.TESTING_EMAIL2})<br>    elif request.method == 'POST':<br>        if request.content_type  != 'application/json':<br>            return HttpResponse(json.dumps({"detail": "Unsupported media type \"'%s'\" in request." % request.content_type}), content_type="application/json",status=401);<br>        # Process request for CSRF<br>        csrf_middleware.process_view(request, None, None, None)<br>        form_data = json.loads(request.body)<br>        form = UserLoginViaOtpFormEmail(form_data)<br>        if form.is_valid():<br>            email = form.cleaned_data.get('email')<br>            response = HttpResponse(<br>                {'email': email},<br>                content_type="application/json"<br>            )<br><br>    remote_form = RemoteForm(form)<br>    # Errors in response_data['non_field_errors'] and response_data['errors']<br>    response_data.update(remote_form.as_dict())<br><br>    response = HttpResponse(<br>        json.dumps(response_data, cls=DjangoJSONEncoder),<br>        content_type="application/json"<br>    )<br><br>    # Process response for CSRF<br>    csrf_middleware.process_response(request, response)<br>    return response<br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image26.png)

 * ## \[code\] urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Add to urlpatterns: /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django/login_register_password/urls.py<br><br>path('api_user_login_via_otp_form_email_django_forms_example',views.api_user_login_via_otp_form_email_django_forms_example,name='api_user_login_via_otp_form_email_django_forms_example')<br></td></tr></tbody></table>

 * ## \[image\] urls.py 

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/login\_register\_password/urls.py

     * ![](images/image21.png)

 * ## \[image\] output after opening the link 

     * http://localhost:8000/login\_register\_password/api\_user\_login\_via\_otp\_form\_email\_django\_forms\_example

     * ![](images/image4.png)

     * \[code\] Commit the changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>## Check git status<br> 19:46:23  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✹<br>$ git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   login_register_password/urls.py<br>        modified:   login_register_password/views.py<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br>## Check git stage changes<br> 19:46:27  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✹<br>$ git add -A<br><br>## Check git commit changes<br> 19:47:21  ✘  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✘ ✚<br>$ git commit -m "Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail"<br>[master 58480ed] Second Commit example: Using Django remote forms: An API endpoint serving remote forms of UserLoginViaOtpFormEmail<br> 2 files changed, 46 insertions(+)<br><br>## push changes<br> 19:48:47  ✘  simha  ...web_dev/DO_NOT_DELETE_djang_basic_documentation_part2/basic_django  🐍 .venv   master ✔<br>$ git push origin master                                                                                                            <br>Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>Enumerating objects: 11, done.<br>Counting objects: 100% (11/11), done.<br>Delta compression using up to 4 threads<br>Compressing objects: 100% (6/6), done.<br>Writing objects: 100% (6/6), 1.19 KiB | 1.19 MiB/s, done.<br>Total 6 (delta 5), reused 0 (delta 0)<br>remote: Resolving deltas: 100% (5/5), completed with 5 local objects.<br>remote: <br>remote: GitHub found 1 vulnerability on sant527/django_basic_documentation_ver2's default branch (1 moderate). To find out more, visit:<br>remote:      https://github.com/sant527/django_basic_documentation_ver2/network/alerts<br>remote: <br>To github.com:sant527/django_basic_documentation_ver2.git<br>   56e04e3..58480ed  master -&gt; master<br></td></tr></tbody></table>

* # Third Commit: Add  node\_module to gitignore

     * Since in the next commit we will be setting up npm which will create node\_modules dir which we want to ignore

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 10:32:08  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git status<br>On branch master<br>nothing to commit, working tree clean<br><br>## NOW DO the changes to .gitignore by adding<br><br># node modules npm init<br>node_modules/<br><br><br> 10:32:19  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git status<br>On branch master<br>Changes not staged for commit:<br>  (use "git add &lt;file&gt;..." to update what will be committed)<br>  (use "git checkout -- &lt;file&gt;..." to discard changes in working directory)<br><br>        modified:   .gitignore<br><br>no changes added to commit (use "git add" and/or "git commit -a")<br><br> 10:33:58  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✹<br>$ git add -A<br><br> 10:34:03  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✘ ✚<br>$ git commit -m "Third Commit: Add  node_module to gitignore"<br>[master a12744b] Third Commit: Add  node_module to gitignore<br> 1 file changed, 4 insertions(+)<br><br> 10:34:15  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git push<br>fatal: The current branch master has no upstream branch.<br>To push the current branch and set the remote as upstream, use<br><br>    git push --set-upstream origin master<br><br> 10:34:45  ✘  simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 .venv   master ✔<br>$ git push --set-upstream origin master                             <br>Enter passphrase for key '/home/simha/.ssh/id_rsa': <br>Enumerating objects: 5, done.<br>Counting objects: 100% (5/5), done.<br>Delta compression using up to 4 threads<br>Compressing objects: 100% (3/3), done.<br>Writing objects: 100% (3/3), 409 bytes | 409.00 KiB/s, done.<br>Total 3 (delta 1), reused 0 (delta 0)<br>remote: Resolving deltas: 100% (1/1), completed with 1 local object.<br>remote: <br>remote: GitHub found 1 vulnerability on sant527/django_basic_documentation_ver2's default branch (1 moderate). To find out more, visit:<br>remote:      https://github.com/sant527/django_basic_documentation_ver2/network/alerts<br>remote: <br>To github.com:sant527/django_basic_documentation_ver2.git<br>   58480ed..a12744b  master -&gt; master<br>Branch 'master' set up to track remote branch 'master' from 'origin'.<br></td></tr></tbody></table>

 * ## \[images\] changing .gitignore

     * ![](images/image13.gif)

     * Now add node\_modules to the .gitignore file

     * ![](images/image52.png)

     * Now commit the changes

     * ![](images/image47.png)![](images/image43.png)

* # Fourth Commit: Setup Nodejs project. Install webpack, webpack-bundle-tracker, react, react-dom, @babel/core babel-loader @babel/preset-env @babel/preset-react and django-webpack-loader (python)

     * Shifting to API based development: To develop mobile applications we cant use web based. Rather we provide the data as JSON and then the mobile application displays it. So on web based apps also we will use data from api rather then loading the web page from backed directly. For that we will use ReactJS as out frontend developer.

     * Reactjs: We will use ReactJs as frontend along with the base template. We will supply the data using api. 

     * webpack: is a module bundler. Its main purpose is to bundle JavaScript files for usage in a browser.

     * Django-webpack-loader: Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

     * [https://github.com/owais/django-webpack-loader](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&sa=D&ust=1577129044715000)

     * Django webpack loader consumes the output generated by webpack-bundle-tracker and lets you use the generated bundles in django.

 * ## Webpack

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Even a simple project contains HTML, CSS and JavaScript files. Also, it can contains assets such as fonts, images, and so on. <br><br>As its core, webpack is a static module bundler. In a particular project, webpack treats all files and assets as modules. Under the hood, it relies on a dependency graph. A dependency graph describes how modules relate to each other using the references (require and import statements) between files. In this way, webpack statically traverses all modules to build the graph, and uses it to generate a single bundle (or several bundles) — a JavaScript file containing the code from all modules combined in the correct order. “Statically” means that, when webpack builds its dependency graph, it doesn’t execute the source code but stitches modules and their dependencies together into a bundle. This can then be included in your HTML files.<br><br>webpack.config.js, which describes how the files and assets should be transformed and what kind of output should be generated.<br><br>Based on the provided configuration, webpack starts from the entry points and resolves each module it encounters while constructing the dependency graph. If a module contains dependencies, the process is performed recursively against each dependency until the traversal has completed. Then webpack bundles all project’s modules into a small number of bundles — usually, just one — to be loaded by the browser.<br></td></tr></tbody></table>

 * ## \[code\] npm init

     * An Absolute Beginner's Guide to Using npm

     * [https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/](https://www.google.com/url?q=https://nodesource.com/blog/an-absolute-beginners-guide-to-using-npm/&sa=D&ust=1577129044717000)

     * npm (originally short for Node Package Manager) is a package manager for the JavaScript programming language.

     * npm init when you're first creating a project. It essentially just creates the package.json

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br><br>$ npm init<br></td></tr></tbody></table>

 * ## \[image\] npm init

     * ![](images/image58.png)![](images/image25.png)

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

     * ![](images/image62.png)![](images/image34.png)

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

     * ![](images/image64.png)![](images/image53.png)![](images/image38.png)![](images/image15.png)

* # FIFTH COMMIT: Setup webpack.config.js, babelrc and settings.py 

     * Also after installing django-webpack-loader python package we have to add to the settings.py

 * ## \[code\] Add webpack\_loader to INSTALLED\_APPS

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>INSTALLED_APPS = (<br>    ...<br>    'webpack_loader',<br>)<br></td></tr></tbody></table>

 * ## \[code\] configuring django-webpack-loader in settings.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>WEBPACK_LOADER = {<br>    'DEFAULT': {<br>        'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.<br>        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>        #BASE_DIR is your Django project directory. The same directory where manage.py is located.<br>    }<br>}<br></td></tr></tbody></table>

 * ## \[images\] diff file

     * ![](images/image5.png)![](images/image45.png)

 * ## \[code\] webpack.config.js

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>NOT SINGLE PAGE APP:<br>We are not creating single page APP. We will have separate .js file for each view<br><br>We will configure our webpack in such a way that it will have different entry points and output points.<br>MULTIPLE ENTRIES<br>For having multiple entry points we have to mention the path in the key name<br>The entry name should be the similar to the django notatio<br><br>BEFORE:<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br><br>AFTER:<br>                        ├── static<br>                        │   └── polls<br>                        │       └── js<br>                        │           ├── bundles<br>                        │           │   ├── index-8ea5b4e40178f2c800ee.js<br>                        │           │   └── question-8ea5b4e40178f2c800ee.js<br>                        │           ├── index.js<br>                        │           └── questions.js<br><br>So example:<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br><br><br>And mention the root folder for output.<br><br>MULTIPLE OUTPUTS<br>For having mutliple outputs we have to use array of configs.<br><br>Example:<br><br>module.exports =[<br>        {<br>          name: "polls",<br>          context: common.context,<br>          entry: entry_output1.entry,<br>          output: entry_output1.output,<br>          plugins: common.plugins,<br>          module: common.module,<br>          resolve: common.resolve,<br>        },<br>           {<br>          name: "login",<br>          context: common.context,<br>          entry: entry_output2.entry,<br>          output: entry_output2.output,<br>          plugins: common.plugins,<br>          module: common.module,<br>          resolve: common.resolve,             <br>           }<br><br>]<br><br>And entry_output1 is:<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br><br><br>And common is:<br><br>common = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br></td></tr></tbody></table>

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var path = require("path");<br>var webpack = require('webpack');<br>var BundleTracker = require('webpack-bundle-tracker');<br><br><br>//the below are the common properties<br>common = {<br>  context: __dirname,<br><br><br>  /* PLUGINS NOTE:<br>  we have installed webpack-bundle-tracker.  npm install --save-dev webpack webpack-bundle-tracker. So we have to add this to the configuration <br>  filename will reside where manager.py resides<br>  Because: django-webpack-loader (python) package setttings.py we set the path as below<br><br>  WEBPACK_LOADER = {<br>      'DEFAULT': {<br>          'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.<br>          'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>          #BASE_DIR is your Django project directory. The same directory where manage.py is located.<br>      }<br>  }<br>  Form above we have to ensure the absolute path of webpack-stats.json is same as os.path.join(BASE_DIR, 'webpack-stats.json')<br>  */<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  /* MODULE Note<br>  we have installed babel-loader: This is a webpack helper which allows to transpile Javascript files with babel and webpack. It uses babel under the hood<br>  What the below configuration does is that for every file with a js or jsx extension, excluding the node_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. <br>  */<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  /* RESOLVE NOTE<br>  Webpack uses resolve.extensions to generate all the possible paths to the module, e.g.<br><br>  function getPaths(module) {<br>      return ['', '.js', '.css'].map(ext =&gt; module + ext);<br>  }<br><br>  getPaths('./somefile'); // ['./somefile', './somefile.js', './somefile.css']<br><br>  getPaths('./somefile.js'); // ['./somefile.js', './somefile.js.js', './somefile.js.css']<br><br>  Webpack would then proceed to lookup each of those paths until it finds a file.<br>  */<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br><br>/* ENTRY OUTPUT EXAMPLE NOTE<br>Example entry ouput object which will be used in the array for module exports<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br>*/<br><br><br>/* MODULE EXPORTS ARRAY NOTE<br> Why are we using array. Because we want different output folders which is not possible<br> with single object<br>*/<br><br>module.exports = [<br>  {<br>    name: "somename",<br>    context: common.context,<br>// Here fill the entry_output<br>/*    entry: entry_output1.entry,<br>    output: entry_output1.output,*/<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,<br>  }<br>]<br><br><br><br><br><br>/* HOW MULTIPLE ENTRY AND OUTPUT WORK NOTE<br>How to set multiple file entry and output in project with webpack?<br>Webpack: path as the entry name: <br><br>EG:<br>pwd: /home/user/project/<br><br>Tree -A<br><br>apps<br>├── dir1<br>│   └── js<br>│       ├── main.js [entry 1]<br>│       └── bundle.js [output 1]<br>└── dir2<br>    ├── index.js [entry 2]<br>    └── foo.js [output 2]<br><br> <br>NOTE dont use / in path.resolve i.e apps/dir1/js/main.js is right /apps/dir1/js/main.js is wrong<br>ERROR in Entry module not found: Error: Can't resolve '/basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js' in '/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2'<br><br>{<br>  entry: {<br>    'dir1/js/bundle': path.resolve(__dirname, 'apps/dir1/js/main.js'),<br>    'dir2/foo' : path.resolve(__dirname, 'apps/dir2/index.js')<br>  },<br>  output: {<br>    path: path.resolve(__dirname, 'apps'),  i.e /home/user/project/apps<br>    filename: '[name]-[hash].js'<br>  },<br>  ...<br>}<br><br>Here  'dir1/js/bundle' is [name] of the entry point. <br><br>Here the important thing is [name] and path  (Use [name] to get the name of the entry point)<br><br>Its like <br>[path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name]-[hash].js'<br>] == [full path]+[name]-[hash].js  == [/home/user/project/apps/]+[dir1/js/bundle]-[jhajkhkd].js = /home/user/project/apps/dir1/js/bundle-jhajkhkd.js<br><br><br>and then stats file become:<br><br>{<br>  "status": "done",<br>  "chunks": {<br><br>    # this is same as the entry name<br>    "dir1/js/bundle": [<br>      {<br><br>        # here name is derived from filename: '[name]-[hash].js' ([name] is entry index name)<br>        "name": "dir1/js/bundle-jhajkhkd.js",<br><br>        # here path is derived from [full path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name].js'] = [path] + [name].js <br>        "path": "/home/user/project/apps/dir1/js/bundle-jhajkhkd.js"<br><br>      }<br>    ],<br>    "dir2/foo": [<br>      {<br>        "name": "dir2/foo.js",<br>        "path": "/home/user/project/apps/dir2/foo-hgjhghjg.js"<br>      }<br>    ]<br>  }<br>}<br><br><br>ALSO ANOTHER EXAMPLE:<br><br><br>NOT SINGLE PAGE APP:<br>We are not creating single page APP. We will have separate .js file for each view<br><br>We will configure our webpack in such a way that it will have different entry points and output points.<br>MULTIPLE ENTRIES<br>For having multiple entry points we have to mention the path in the key name<br>The entry name should be the similar to the django notatio<br><br>BEFORE:<br>                    ├── static<br>                    │   └── polls<br>                    │       └── js<br>                    │           ├── index.js<br>                    │           └── questions.js<br><br>AFTER:<br>                        ├── static<br>                        │   └── polls<br>                        │       └── js<br>                        │           ├── bundles<br>                        │           │   ├── index-8ea5b4e40178f2c800ee.js<br>                        │           │   └── question-8ea5b4e40178f2c800ee.js<br>                        │           ├── index.js<br>                        │           └── questions.js<br><br>So example:<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br><br><br>And mention the root folder for output.<br><br>MULTIPLE OUTPUTS<br>For having mutliple outputs we have to use array of configs.<br><br>Example:<br><br>module.exports =[<br>  {<br>    name: "polls",<br>    context: common.context,<br>    entry: entry_output1.entry,<br>    output: entry_output1.output,<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,<br>  },<br>           {<br>    name: "login",<br>    context: common.context,<br>    entry: entry_output2.entry,<br>    output: entry_output2.output,<br>    plugins: common.plugins,<br>    module: common.module,<br>    resolve: common.resolve,             <br>           }<br><br>]<br><br>And entry_output1 is:<br>entry_output1 = {<br><br>  entry: {<br>    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),<br>    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),<br>   },<br><br>  output: {<br>    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end<br>    filename: "[name]-[hash].js",<br>  }<br>}<br><br><br>And common is:<br><br>common = {<br>  context: __dirname,<br><br>  plugins: [<br>    new BundleTracker({filename: './basic_django/webpack-stats.json'}),<br>  ],<br><br>  module: {<br>    rules: [<br>      {<br>        test: /.(js|jsx)$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br><br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>}<br><br>*/<br><br></td></tr></tbody></table>

 * ## \[image\] webpack config

     * ![](images/image18.png)![](images/image68.png)![](images/image7.png)![](images/image1.png)![](images/image27.png)![](images/image50.png)![](images/image51.png)![](images/image44.png)![](images/image56.png)

 * ## \[code\] .Babelrc for reactjs and  babel-loader(already added above but just shown) to webpack.config.js 

     * We also need to setup our babel config file, create a new file in the root directory called .babelrc and write the following configuration to it

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>Cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br>Touch .babelrc (we have already created .babelrc in the previous commit)<br></td></tr></tbody></table>

     * .babelrc

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>{<br>  "presets": ["@babel/preset-env", "@babel/preset-react"]<br>}<br><br></td></tr></tbody></table>

     * The above configuration will ensure that babel transpiles our react code, which is JSX and any other ES6+ code we have to ES5 code.

 * ## \[image\] .babelrc

     * ![](images/image66.png)

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

     * ![](images/image54.png)![](images/image29.png)![](images/image40.png)![](images/image28.png)![](images/image61.png)![](images/image23.png)

 * ## \[code\] Generate the bundle js using webpack and runserver and check whether the reactjs is working

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ Cd /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2<br>$ ./node_modules/.bin/webpack --config webpack.config.js<br>$ cd basic_django<br>$ python manage.py runserver <br><br>localhost:8000/polls_webpack_react_example<br>localhost:8000/polls_webpack_react_example/questions<br></td></tr></tbody></table>

 * ## \[image\] generate bundle and runserver and check urls

     * ![](images/image36.png)![](images/image41.png)

 * ## \[code\] Then add to the urls of of the project

     * /home/web\_dev/DO\_NOT\_DELETE\_djang\_basic\_documentation\_part2/basic\_django/basic\_django/urls.py

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>from django.contrib import admin<br>from django.urls import path, include<br><br>urlpatterns = [<br>…<br>    path('polls_webpack_react_example/', include('polls_example_for_webpack_and_reactjs.polls.urls')),<br>...<br>]<br></td></tr></tbody></table>

 * ## \[code\] After starting the server open the links:

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>localhost:8000/polls_webpack_react_example<br>localhost:8000/polls_webpack_react_example/questions<br></td></tr></tbody></table>

 * ## \[code\] commit changes

     * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td> 23:16:41  ⚙ simha  /home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2  🐍 DO_NOT_DELETE_djang_basic_documentation_pa-kHaUQTsF   master ✘ ⬇ ⬆ ✚<br>$ git status<br>On branch master<br>Your branch and 'origin/master' have diverged,<br>and have 3 and 3 different commits each, respectively.<br>  (use "git pull" to merge the remote branch into yours)<br><br>Changes to be committed:<br>  (use "git reset HEAD &lt;file&gt;..." to unstage)<br><br>        modified:   basic_django/basic_django/settings.py<br>        modified:   basic_django/basic_django/urls.py<br>        new file:   basic_django/custom_user/migrations/0004_auto_20191222_1300.py<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/migrations/0001_initial.py<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/index-ff981c23bdb4b0ef93e3.js<br>        new file:   basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/questions-ff981c23bdb4b0ef93e3.js<br>        new file:   basic_django/webpack-stats.json<br>        modified:   package-lock.json<br>        modified:   package.json<br>        modified:   webpack.config.js<br><br><br>$ git commit -m "Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app"<br>[master f603b9c] Seventh Commit B: Example of webpack and Reactjs:: Setting the polls app<br> 10 files changed, 762 insertions(+), 46 deletions(-)<br> create mode 100644 basic_django/custom_user/migrations/0004_auto_20191222_1300.py<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/migrations/0001_initial.py<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/index-ff981c23bdb4b0ef93e3.js<br> create mode 100644 basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/bundles/questions-ff981c23bdb4b0ef93e3.js<br> create mode 100644 basic_django/webpack-stats.json<br><br></td></tr></tbody></table>

 * ## \[image\]

     * ![](images/image9.png)

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

     * [https://github.com/owais/django-webpack-loader/issues/177](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader/issues/177&sa=D&ust=1577129044849000)

     * polls app: we want to have two bundled js for index and questions html pages.

     * Project structure:

     * ![](images/image30.png)

     * ### \[code\] settings.py

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>STATIC_URL = '/static/'<br><br>WEBPACK_LOADER = {<br>    'DEFAULT': {<br>        'BUNDLE_DIR_NAME': '',<br>        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),<br>        # '/home/web_dev/krishnacook_pipenv/webpack-stats.json'<br>    }<br>}<br></td></tr></tbody></table>

     * ### \[code\] Webpack.config.js:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>var path = require("path");<br>var webpack = require('webpack');<br>var BundleTracker = require('webpack-bundle-tracker');<br><br>module.exports = {<br>  context: __dirname,<br><br>// mention the path in the key name (refer to the webpack multiple entries<br><br>  entry: {<br>    'polls/bundles/index':  './src/polls/static/polls/js/index',<br>    'polls/bundles/questions':  './src/polls/static/polls/js/questions',<br>   },<br><br>  output: {<br>    path: path.join(__dirname, '/src/polls/static/'),<br>    filename: "[name]-[hash].js",<br>  },<br><br>  // output: {<br>  //     path: path.resolve('./src/polls/static/bundles/'),<br>  //     filename: "[name]-[hash].js",<br>  // },<br><br>  plugins: [<br>    new BundleTracker({filename: './src/webpack-stats.json'}),<br>  ],<br>  module: {<br>    rules: [<br>      {<br>        test: /\.js$/,<br>        exclude: /node_modules/,<br>        use: {<br>          loader: "babel-loader"<br>        }<br>      }<br>    ]<br>  },<br>  resolve: {<br>    extensions: ['*', '.js', '.jsx']<br>  }<br><br>};<br></td></tr></tbody></table>

     * ### \[image\] webpack.config.js

       * ![](images/image19.png)![](images/image10.png)

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

 * ## Django-webpack-loader: [https://github.com/owais/django-webpack-loader](https://www.google.com/url?q=https://github.com/owais/django-webpack-loader&sa=D&ust=1577129044888000)

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

       * ![](images/image42.png)

     * ### \[code\] correct way to resize the terminator

       * ![](images/image65.png)

 * ## Create a file called terminator\_screenshot.sh and copy the script into it

     * ### \[code\] terminator screen shot script

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>set -x -o verbose;<br>export DISPLAY=:0.0 &amp;&amp;<br><br>#### important<br># Before running this script ensure that the size of the terminal is manually fit <br># to the cursor button.<br><br># the below is to get the recent seen window in a group of windows<br>xdotool search  --desktop 0 --class Terminator<br>windowid=$(xdotool search  --desktop 0 --class Terminator | awk 'END{print}'); <br>width_ter=`xdotool getwindowgeometry $windowid | awk '/Geometry/' | awk '{match($0,/Geometry: ([0-9]+)x([0-9]+)/,a); print a[1]}'`<br>height_ter=`xdotool getwindowgeometry $windowid | awk '/Geometry/' | awk '{match($0,/Geometry: ([0-9]+)x([0-9]+)/,a); print a[2]}'`<br>echo $width_ter<br>echo $height_ter<br><br>xdotool windowactivate ${windowid} &amp;&amp;<br><br>#crop_a=$((21)) # this is for not tabs<br>#crop_a=$((0)) # this is for not tabs<br>crop_a=$((21+36)) # this is for tabs<br>crop_b=$((1)) # this is for tabs<br><br>DIR="/home/simha/terminator_screenshots"<br># init<br># look for empty dir <br>if [ "$(ls -A $DIR)" ]; then<br>   echo "Take action $DIR is not Empty"<br>else<br>   echo "$DIR is Empty"<br>   filename="$(date +%Y-%m-%d-%H_%M_%S).png"<br>   echo $filename<br>   import -window ${windowid} -crop +0+${crop_a} -crop +0-${crop_b} /home/simha/terminator_screenshots/${filename}<br>fi<br><br><br>sleep 1<br><br>echo "MotionNotify 508 251" &gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrPress Shift_L" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "Delay 400" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrPress Prior" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrRelease Prior" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "Delay 408" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br>echo "KeyStrRelease Shift_L" &gt;&gt; /home/simha/.public_html/xmacros_terminator_screenshot<br><br>xmacroplay &lt; "/home/simha/.public_html/xmacros_terminator_screenshot"<br><br>filename="$(date +%Y-%m-%d-%H_%M_%S).png"<br>echo $filename<br>import -window ${windowid} -crop +0+${crop_a} -crop +0-${crop_b}  /home/simha/terminator_screenshots/${filename}<br><br>gwenview /home/simha/terminator_screenshots/${filename}<br><br></td></tr></tbody></table>

     * ### \[image\] terminator screenshot script

       * ![](images/image73.png)

 * ## Create a keyboard shortcut for this script in KDE desktop env

     * In kde got to edit applications and create a keyboard shortcut for this script. (i have created WIN + h)

 * ## Start taking screenshots

     * Now after resizing the terminator properly press the shortcut key and it will take a screenshot and move the screen up. If we want to take more screen shot again press the shortcut key and keep doing this till the time you want.

 * ## Combine the screenshots

     * All the screenshots will be stored in the folder /home/simha/terminator\_screenshots

     * ### \[code\] To combine all the images into one use the following command:

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>#gauranga<br>$ convert -append $(ls -1 *.png | sort -r) out.png<br></td></tr></tbody></table>

     * ### \[image\] to combine all the images into one

       * ![](images/image17.png)

 * ## Break images into multiple images for the purpose of using them in google docs

     * If the image is long we have to break it into multiple images. Else google docs when converting it into html it will show low res images. For that we run the following script

     * ### \[code\] splitting the images vertically with aspect ratio of 900:600

       * <table><colgroup><col style="width: 100%" /></colgroup><tbody><tr class="odd"><td>$ filename="git_stashing_usage.png"               <br>rm -rf ~/croped &amp;&amp;<br>mkdir ~/croped &amp;&amp;<br>width=`identify -format '%w' ${filename}`<br>echo "width= $width"<br>height=`identify -format '%h' ${filename}`<br>echo "height= $height"<br><br>a=`echo "scale=10; ((900/$width) * $height)/600" | bc`<br>echo $a<br><br>rem=`echo "scale=1; $a % 1" | bc`<br>echo $rem<br>int1=`echo "($height*$width)/(600*900)" | bc`<br>echo $int1<br>int2=$(( $int1 + 1))<br>echo $int2<br><br>st=$((`echo "$rem &lt; 0.3"| bc`))<br>echo "st= $st"<br>if [ $st -eq 1 ]; then<br>        echo "$rem &lt; 0.3"<br>    convert -crop 1x${int1}+0+8@ ${filename} ~/croped/crop_grid_%d.png<br>else<br>        echo "$rem &gt; 0.3"<br>        convert -crop 1x${int2}+0+8@ ${filename} ~/croped/crop_grid_%d.png<br>fi<br><br>pcmanfm /home/simha/croped<br></td></tr></tbody></table>

     * ### \[image\] splitting images vertically

       * ![](images/image8.png)

 * ## Paste them into the google docs:

     * Once the images are split then we can paste them into the google docs.

 * ## Using gimp to split images using guides and keep required images and then combine them.

     * Sometimes we want to split an image using guides. This can be done using gimp. Go to Filters \> web \> Slice. Then save the split images into a folder.

     * Delete the unwanted images and then combine them using

     * $ convert -append $(ls -1 \*.png) out.png

 * ## Django putting all the apps in subfolder:

     * [https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error](https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&sa=D&ust=1577129044931000)[r](https://www.google.com/url?q=https://stackoverflow.com/questions/3948356/how-to-keep-all-my-django-applications-in-specific-folder&sa=D&ust=1577129044931000)

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

       * [https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder](https://www.google.com/url?q=https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder&sa=D&ust=1577129044938000)

       * [https://stackoverflow.com/a/6649433/2897115](https://www.google.com/url?q=https://stackoverflow.com/a/6649433/2897115&sa=D&ust=1577129044939000)

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

     * ### \[images\] [https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error](https://www.google.com/url?q=https://stackoverflow.com/questions/10313475/moving-django-apps-into-subfolder-and-url-py-error&sa=D&ust=1577129044948000)

       * ![](images/image14.png)![](images/image37.png)![](images/image72.png)![](images/image69.png)

     * ### \[images\] how to tackle with testing error when using subfolders https://stackoverflow.com/questions/6483636/how-to-test-django-application-placed-in-subfolder

       * ![](images/image12.png)![](images/image11.png)![](images/image49.png)![](images/image33.png)![](images/image16.png)

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

       * ![](images/image24.png)![](images/image63.png)

