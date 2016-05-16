/*global require*/
(function (r) {
    "use strict";
    var scss = r("gulp-sass"),
    gulp = r("gulp");

    gulp.task("scss", function () {
        gulp.src(
            "./src/scss/main.scss"
        ).pipe(scss(
            {"bundleExec": true}
        )).pipe(gulp.dest("./static/css"));
    });

    gulp.task('watch', function() {
      gulp.watch('./src/scss/*.scss', ['scss']);
    });
}(require));