var gulp = require('gulp'),
    plumber = require('gulp-plumber'),
    rename = require('gulp-rename');
var autoprefixer = require('gulp-autoprefixer');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin'),
    cache = require('gulp-cache');
var minifycss = require('gulp-minify-css');
var stylus = require('gulp-stylus');

gulp.task('images', function () {
    gulp.src('src/images/**/*')
        .pipe(cache(imagemin({optimizationLevel: 3, progressive: true, interlaced: true})))
        .pipe(gulp.dest('staticfiles/dist/images/'));
});

gulp.task('styles', function () {
    gulp.src(['src/styles/main.styl'])
        .pipe(plumber({
            errorHandler: function (error) {
                console.log(error.message);
                this.emit('end');
            }
        }))
        .pipe(stylus({
            'include css': true,
            compress: true,
            linenos: true
        }))
        .pipe(autoprefixer('last 2 versions'))
        .pipe(gulp.dest('dist/styles/'))
        .pipe(rename({suffix: '.min'}))
        .pipe(minifycss())
        .pipe(gulp.dest('staticfiles/dist/styles/'))
});

gulp.task('scripts', function () {
    return gulp.src(['src/scripts/libs/jQuery_v3.3.1.js', 'src/scripts/libs/uikit.js', 'src/scripts/libs/uikit-icons.js', 'src/scripts/back.js', 'src/scripts/front.js'])
        .pipe(plumber({
            errorHandler: function (error) {
                console.log(error.message);
                this.emit('end');
            }
        }))
        .pipe(concat('main.js'))
        .pipe(gulp.dest('staticfiles/dist/scripts/'))
        .pipe(rename({suffix: '.min'}))
        .pipe(uglify())
        .pipe(gulp.dest('staticfiles/dist/scripts/'))
});

gulp.task('default', function () {
    gulp.watch("src/styles/**/*.styl", ['styles']);
    gulp.watch("src/scripts/**/*.js", ['scripts']);
});
