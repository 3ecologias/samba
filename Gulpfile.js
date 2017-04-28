var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('sass', function () {
  return gulp.src('./static/sass/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./static/'));
});

gulp.task('watch', function () {
  gulp.watch('./static/sass/**/*.scss', ['sass']);
})

gulp.task('build', ['sass']);
