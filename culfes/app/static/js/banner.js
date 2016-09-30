/*! modernizr 3.2.0 (Custom Build) | MIT *
 * http://modernizr.com/download/?-cssanimations-prefixed !*/
! function(e, n, t) {
    function r(e, n) {
        return typeof e === n
    }

    function o() {
        var e, n, t, o, i, s, f;
        for (var a in y)
            if (y.hasOwnProperty(a)) {
                if (e = [], n = y[a], n.name && (e.push(n.name.toLowerCase()), n.options && n.options.aliases && n.options.aliases.length))
                    for (t = 0; t < n.options.aliases.length; t++) e.push(n.options.aliases[t].toLowerCase());
                for (o = r(n.fn, "function") ? n.fn() : n.fn, i = 0; i < e.length; i++) s = e[i], f = s.split("."), 1 === f.length ? Modernizr[f[0]] = o : (!Modernizr[f[0]] || Modernizr[f[0]] instanceof Boolean || (Modernizr[f[0]] = new Boolean(Modernizr[f[0]])), Modernizr[f[0]][f[1]] = o), C.push((o ? "" : "no-") + f.join("-"))
            }
    }

    function i(e) {
        return e.replace(/([a-z])-([a-z])/g, function(e, n, t) {
            return n + t.toUpperCase()
        }).replace(/^-/, "")
    }

    function s(e, n) {
        return !!~("" + e).indexOf(n)
    }

    function f(e, n) {
        return function() {
            return e.apply(n, arguments)
        }
    }

    function a(e, n, t) {
        var o;
        for (var i in e)
            if (e[i] in n) return t === !1 ? e[i] : (o = n[e[i]], r(o, "function") ? f(o, t || n) : o);
        return !1
    }

    function u(e) {
        return e.replace(/([A-Z])/g, function(e, n) {
            return "-" + n.toLowerCase()
        }).replace(/^ms-/, "-ms-")
    }

    function l() {
        return "function" != typeof n.createElement ? n.createElement(arguments[0]) : z ? n.createElementNS.call(n, "http://www.w3.org/2000/svg", arguments[0]) : n.createElement.apply(n, arguments)
    }

    function p() {
        var e = n.body;
        return e || (e = l(z ? "svg" : "body"), e.fake = !0), e
    }

    function d(e, t, r, o) {
        var i, s, f, a, u = "modernizr",
            d = l("div"),
            c = p();
        if (parseInt(r, 10))
            for (; r--;) f = l("div"), f.id = o ? o[r] : u + (r + 1), d.appendChild(f);
        return i = l("style"), i.type = "text/css", i.id = "s" + u, (c.fake ? c : d).appendChild(i), c.appendChild(d), i.styleSheet ? i.styleSheet.cssText = e : i.appendChild(n.createTextNode(e)), d.id = u, c.fake && (c.style.background = "", c.style.overflow = "hidden", a = E.style.overflow, E.style.overflow = "hidden", E.appendChild(c)), s = t(d, e), c.fake ? (c.parentNode.removeChild(c), E.style.overflow = a, E.offsetHeight) : d.parentNode.removeChild(d), !!s
    }

    function c(n, r) {
        var o = n.length;
        if ("CSS" in e && "supports" in e.CSS) {
            for (; o--;)
                if (e.CSS.supports(u(n[o]), r)) return !0;
            return !1
        }
        if ("CSSSupportsRule" in e) {
            for (var i = []; o--;) i.push("(" + u(n[o]) + ":" + r + ")");
            return i = i.join(" or "), d("@supports (" + i + ") { #modernizr { position: absolute; } }", function(e) {
                return "absolute" == getComputedStyle(e, null).position
            })
        }
        return t
    }

    function m(e, n, o, f) {
        function a() {
            p && (delete b.style, delete b.modElem)
        }
        if (f = r(f, "undefined") ? !1 : f, !r(o, "undefined")) {
            var u = c(e, o);
            if (!r(u, "undefined")) return u
        }
        for (var p, d, m, h, v, y = ["modernizr", "tspan"]; !b.style;) p = !0, b.modElem = l(y.shift()), b.style = b.modElem.style;
        for (m = e.length, d = 0; m > d; d++)
            if (h = e[d], v = b.style[h], s(h, "-") && (h = i(h)), b.style[h] !== t) {
                if (f || r(o, "undefined")) return a(), "pfx" == n ? h : !0;
                try {
                    b.style[h] = o
                } catch (g) {}
                if (b.style[h] != v) return a(), "pfx" == n ? h : !0
            }
        return a(), !1
    }

    function h(e, n, t, o, i) {
        var s = e.charAt(0).toUpperCase() + e.slice(1),
            f = (e + " " + x.join(s + " ") + s).split(" ");
        return r(n, "string") || r(n, "undefined") ? m(f, n, o, i) : (f = (e + " " + S.join(s + " ") + s).split(" "), a(f, n, t))
    }

    function v(e, n, r) {
        return h(e, t, t, n, r)
    }
    var y = [],
        g = {
            _version: "3.2.0",
            _config: {
                classPrefix: "",
                enableClasses: !0,
                enableJSClass: !0,
                usePrefixes: !0
            },
            _q: [],
            on: function(e, n) {
                var t = this;
                setTimeout(function() {
                    n(t[e])
                }, 0)
            },
            addTest: function(e, n, t) {
                y.push({
                    name: e,
                    fn: n,
                    options: t
                })
            },
            addAsyncTest: function(e) {
                y.push({
                    name: null,
                    fn: e
                })
            }
        },
        Modernizr = function() {};
    Modernizr.prototype = g, Modernizr = new Modernizr;
    var C = [],
        w = "Moz O ms Webkit",
        x = g._config.usePrefixes ? w.split(" ") : [];
    g._cssomPrefixes = x;
    var _ = function(n) {
        var r, o = prefixes.length,
            i = e.CSSRule;
        if ("undefined" == typeof i) return t;
        if (!n) return !1;
        if (n = n.replace(/^@/, ""), r = n.replace(/-/g, "_").toUpperCase() + "_RULE", r in i) return "@" + n;
        for (var s = 0; o > s; s++) {
            var f = prefixes[s],
                a = f.toUpperCase() + "_" + r;
            if (a in i) return "@-" + f.toLowerCase() + "-" + n
        }
        return !1
    };
    g.atRule = _;
    var S = g._config.usePrefixes ? w.toLowerCase().split(" ") : [];
    g._domPrefixes = S;
    var E = n.documentElement,
        z = "svg" === E.nodeName.toLowerCase(),
        P = {
            elem: l("modernizr")
        };
    Modernizr._q.push(function() {
        delete P.elem
    });
    var b = {
        style: P.elem.style
    };
    Modernizr._q.unshift(function() {
        delete b.style
    }), g.testAllProps = h;
    g.prefixed = function(e, n, t) {
        return 0 === e.indexOf("@") ? _(e) : (-1 != e.indexOf("-") && (e = i(e)), n ? h(e, n, t) : h(e, "pfx"))
    };
    g.testAllProps = v, Modernizr.addTest("cssanimations", v("animationName", "a", !0)), o(), delete g.addTest, delete g.addAsyncTest;
    for (var T = 0; T < Modernizr._q.length; T++) Modernizr._q[T]();
    e.Modernizr = Modernizr
}(window, document);

/**
 * index banner
 */
 var banner = (function() { 
	var	$main = $( '.banner' ),
		$pages = $main.children( 'div.banner_img' ),
		animcursor = 1,
		pagesCount = $pages.length,
		current = 0,
        next = 0,
		isAnimating = false,
		endCurrPage = false,
		endNextPage = false,
		animEndEventNames = {
			'WebkitAnimation' : 'webkitAnimationEnd',
			'OAnimation' : 'oAnimationEnd',
			'msAnimation' : 'MSAnimationEnd',
			'animation' : 'animationend'
		},
		// animation end event name
		animEndEventName = animEndEventNames[ Modernizr.prefixed( 'animation' ) ],
		// support css animations
		support = Modernizr.cssanimations;
        var dots = document.querySelectorAll('.banner .dot');
        dots[current].className += ' current_dot ';
    //init
	function init() {
		$pages.each( function() {
			var $page = $( this );
			$page.data( 'originalClassList', $page.attr( 'class' ) );
		} );

		$pages.eq( current ).addClass( 'current' );

		 function auto () {
			if( isAnimating ) {
				return false;
			}
            if( current < pagesCount - 1 ) {
                next = current+1;
            }
            else {
                next = 0;
            }
			nextPage( animcursor );
		} 
		window.setInterval(auto,6000);
		for( var i = 0; i < pagesCount; i++ ){      	
    	    manaul(dots[i], i);
		}
	}
	//manaul
	function manaul (dot,j){
		dot.addEventListener("click",function(){
			if( isAnimating ) {
				return false;
			}
			if( j > current ) {
				animcursor = 1;
			}
			if( j < current ) {
				animcursor = 2;
			}
		    next = j;
			nextPage( animcursor );
		});
	}
	function nextPage( animation ) {
		if( isAnimating ) {
			return false;
		}
        if( current == next ) {
            return false;
        }
		isAnimating = true;
		var $currPage = $pages.eq( current );
        dots[current].className = dots[current].className.replace( /current_dot/,' ' );
		current = next;
		var $nextPage = $pages.eq( current ).addClass( 'current' ),	
			outClass = '', inClass = '';
        dots[current].className += ' current_dot ';
		switch( animation ) {
			case 1:
				outClass = 'rtl_next';
                inClass = 'rtl_prev';
                break;
			case 2:
				outClass = 'ltr_next';
                inClass = 'ltr_prev';
                break;
            case 0:
                break;
		}
		$currPage.addClass( outClass ).on( animEndEventName, function() {
			$currPage.off( animEndEventName );
			endCurrPage = true;
			if( endNextPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );
		$nextPage.addClass( inClass ).on( animEndEventName, function() {
			$nextPage.off( animEndEventName );
			endNextPage = true;
			if( endCurrPage ) {
				onEndAnimation( $currPage, $nextPage );
			}
		} );
		if( !support ) {
			onEndAnimation( $currPage, $nextPage );
		}
	}
	function onEndAnimation( $outpage, $inpage ) {
		endCurrPage = false;
		endNextPage = false;
		resetPage( $outpage, $inpage );
		isAnimating = false;
	}
	function resetPage( $outpage, $inpage ) {
		$outpage.attr( 'class', $outpage.data( 'originalClassList' ) );
		$inpage.attr( 'class', $inpage.data( 'originalClassList' ) + ' current' );
	}
	init();
	return { init : init };
})();

