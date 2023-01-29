// Initialize modules
const { src, dest, watch, series, parallel } = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const concat = require('gulp-concat');
const cssnano = require('cssnano');
const postcss = require('gulp-postcss');
const replace = require('gulp-replace');
const uglify = require('gulp-uglify');

// File path varialbes
const files = {
    indexScssPath: '_frontend/scss/index.scss',
    scssPath: '_frontend/scss/**/*.scss',
    jsPath: '_frontend/js/**/*.js'
}
// Sass task
const scssTask = () => {
    return src(files.indexScssPath, { sourcemaps: true})
        .pipe(sass())
        .pipe(postcss([cssnano()]))
        .pipe(dest('shared/static/css', { sourcemaps: '.' }))
}

// JS task
const jsTask = () => {
    return src(files.jsPath)
        .pipe(concat('main.js'))
        .pipe(uglify())
        .pipe(dest('shared/static/js'))
}

// Cachebusting task
const chacheBustTask = () => {
    let cbString = new Date().getTime()
    return src(['shared/templates/base.html'])
        .pipe(replace(/cb=\d+/g, 'cb=' + cbString))
        .pipe(dest('shared/templates'))
}       

// Watch task
const watchTask = () => {
    watch([files.scssPath, files.jsPath],
        parallel(scssTask, jsTask));
}

// Default task

exports.default = series(
    parallel(scssTask, jsTask),
    chacheBustTask,
    watchTask
)