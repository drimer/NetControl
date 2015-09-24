module.exports = function (grunt) {
    "use strict";

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        bower: {
            install: {
                options: {
                    targetDir: './app/lib',
                    install: true,
                    cleanTargetDir: false,
                    cleanBowerDir: true,
                    bowerOptions: {}
                }
            }
        }
    });

    grunt.loadNpmTasks('grunt-bower-task');

    grunt.registerTask('default', ['']);
};