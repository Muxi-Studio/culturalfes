/*global require*/
(function (r) {
    "use strict";
    var scss = r("gulp-sass"),
    gulp = r("gulp"),
    livereload = require('gulp-livereload');

    gulp.task("scss", function () {
        gulp.src(
            "./src/scss/main.scss"
        ).pipe(scss(
            {"bundleExec": true}
        )).pipe(gulp.dest("./static/css"))
        .pipe(livereload());
    });

    gulp.task('watch', function() {
    livereload.listen();
      gulp.watch('./src/scss/*.scss', ['scss']);
    });
}(require));