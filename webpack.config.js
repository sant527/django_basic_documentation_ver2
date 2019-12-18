var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');


//the below are the common properties
common = {
  context: __dirname,


  /* PLUGINS NOTE:
  we have installed webpack-bundle-tracker.  npm install --save-dev webpack webpack-bundle-tracker. So we have to add this to the configuration 
  filename will reside where manager.py resides
  Because: django-webpack-loader (python) package setttings.py we set the path as below

  WEBPACK_LOADER = {
      'DEFAULT': {
          'BUNDLE_DIR_NAME': '',  #we want to have multiple entry in webpack so we keep this blank.
          'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
          #BASE_DIR is your Django project directory. The same directory where manage.py is located.
      }
  }
  Form above we have to ensure the absolute path of webpack-stats.json is same as os.path.join(BASE_DIR, 'webpack-stats.json')
  */

  plugins: [
    new BundleTracker({filename: './basic_django/webpack-stats.json'}),
  ],

  /* MODULE Note
  we have installed babel-loader: This is a webpack helper which allows to transpile Javascript files with babel and webpack. It uses babel under the hood
  What the below configuration does is that for every file with a js or jsx extension, excluding the node_modules folder and it's content, webpack uses babel-loader to transpile the ES6 code to ES5. 
  */

  module: {
    rules: [
      {
        test: /.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },

  /* RESOLVE NOTE
  Webpack uses resolve.extensions to generate all the possible paths to the module, e.g.

  function getPaths(module) {
      return ['', '.js', '.css'].map(ext => module + ext);
  }

  getPaths('./somefile'); // ['./somefile', './somefile.js', './somefile.css']

  getPaths('./somefile.js'); // ['./somefile.js', './somefile.js.js', './somefile.js.css']

  Webpack would then proceed to lookup each of those paths until it finds a file.
  */

  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

}

/* ENTRY OUTPUT EXAMPLE NOTE
Example entry ouput object which will be used in the array for module exports
entry_output1 = {

  entry: {
    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),
    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),
   },

  output: {
    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end
    filename: "[name]-[hash].js",
  }
}
*/


/* MODULE EXPORTS ARRAY NOTE
 Why are we using array. Because we want different output folders which is not possible
 with single object
*/

module.exports = [
  {
    name: "somename",
    context: common.context,
// Here fill the entry_output
/*    entry: entry_output1.entry,
    output: entry_output1.output,*/
    plugins: common.plugins,
    module: common.module,
    resolve: common.resolve,
  }
]





/* HOW MULTIPLE ENTRY AND OUTPUT WORK NOTE
How to set multiple file entry and output in project with webpack?
Webpack: path as the entry name: 

EG:
pwd: /home/user/project/

Tree -A

apps
├── dir1
│   └── js
│       ├── main.js [entry 1]
│       └── bundle.js [output 1]
└── dir2
    ├── index.js [entry 2]
    └── foo.js [output 2]

 
NOTE dont use / in path.resolve i.e apps/dir1/js/main.js is right /apps/dir1/js/main.js is wrong
ERROR in Entry module not found: Error: Can't resolve '/basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js' in '/home/web_dev/DO_NOT_DELETE_djang_basic_documentation_part2'

{
  entry: {
    'dir1/js/bundle': path.resolve(__dirname, 'apps/dir1/js/main.js'),
    'dir2/foo' : path.resolve(__dirname, 'apps/dir2/index.js')
  },
  output: {
    path: path.resolve(__dirname, 'apps'),  i.e /home/user/project/apps
    filename: '[name]-[hash].js'
  },
  ...
}

Here  'dir1/js/bundle' is [name] of the entry point. 

Here the important thing is [name] and path  (Use [name] to get the name of the entry point)

Its like 
[path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name]-[hash].js'
] == [full path]+[name]-[hash].js  == [/home/user/project/apps/]+[dir1/js/bundle]-[jhajkhkd].js = /home/user/project/apps/dir1/js/bundle-jhajkhkd.js


and then stats file become:

{
  "status": "done",
  "chunks": {

    # this is same as the entry name
    "dir1/js/bundle": [
      {

        # here name is derived from filename: '[name]-[hash].js' ([name] is entry index name)
        "name": "dir1/js/bundle-jhajkhkd.js",

        # here path is derived from [full path]+[filename] == [path: path.resolve(__dirname, '/apps')] + [filename: '[name].js'] = [path] + [name].js 
        "path": "/home/user/project/apps/dir1/js/bundle-jhajkhkd.js"

      }
    ],
    "dir2/foo": [
      {
        "name": "dir2/foo.js",
        "path": "/home/user/project/apps/dir2/foo-hgjhghjg.js"
      }
    ]
  }
}


ALSO ANOTHER EXAMPLE:


NOT SINGLE PAGE APP:
We are not creating single page APP. We will have separate .js file for each view

We will configure our webpack in such a way that it will have different entry points and output points.
MULTIPLE ENTRIES
For having multiple entry points we have to mention the path in the key name
The entry name should be the similar to the django notatio

BEFORE:
                    ├── static
                    │   └── polls
                    │       └── js
                    │           ├── index.js
                    │           └── questions.js

AFTER:
                        ├── static
                        │   └── polls
                        │       └── js
                        │           ├── bundles
                        │           │   ├── index-8ea5b4e40178f2c800ee.js
                        │           │   └── question-8ea5b4e40178f2c800ee.js
                        │           ├── index.js
                        │           └── questions.js

So example:

  entry: {
    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),
    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),
   },

  output: {
    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end
    filename: "[name]-[hash].js",
  }


And mention the root folder for output.

MULTIPLE OUTPUTS
For having mutliple outputs we have to use array of configs.

Example:

module.exports =[
  {
    name: "polls",
    context: common.context,
    entry: entry_output1.entry,
    output: entry_output1.output,
    plugins: common.plugins,
    module: common.module,
    resolve: common.resolve,
  },
           {
    name: "login",
    context: common.context,
    entry: entry_output2.entry,
    output: entry_output2.output,
    plugins: common.plugins,
    module: common.module,
    resolve: common.resolve,             
           }

]

And entry_output1 is:
entry_output1 = {

  entry: {
    'polls/js/bundles/index':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/index.js'),
    'polls/js/bundles/questions':  path.resolve(__dirname, 'basic_django/polls_example_for_webpack_and_reactjs/polls/static/polls/js/questions.js'),
   },

  output: {
    path: path.join(__dirname)+"/basic_django/polls_example_for_webpack_and_reactjs/polls/static/", // add / at the end
    filename: "[name]-[hash].js",
  }
}


And common is:

common = {
  context: __dirname,

  plugins: [
    new BundleTracker({filename: './basic_django/webpack-stats.json'}),
  ],

  module: {
    rules: [
      {
        test: /.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  },

  resolve: {
    extensions: ['*', '.js', '.jsx']
  }

}

*/