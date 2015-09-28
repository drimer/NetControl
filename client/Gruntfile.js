module.exports = function (grunt) {
    "use strict";

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        bower: {
            install: {
                options: {
                    targetDir: './lib',
                    install: true,
                    cleanTargetDir: false,
                    cleanBowerDir: true,
                    bowerOptions: {}
                }
            }
        },

        concat: {
            web: {
                src: [
                    "src/*.css"
                ],
                dest: "app/app.css"
            }
        },

        less: {
            development: {
                files: {
                    "app/app.css": [
                        "src/*.less"
                    ]
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-bower-task');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-less');

    grunt.registerTask('default', ['bower', 'less']);
};