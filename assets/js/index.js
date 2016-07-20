var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory
var Config = require('Config')


var Welcome1 = React.createClass({
    render: function () {
        return (
            <div className="page-content-wrapper text-09">
                <div className="container-fluid">
                    <div className="row title-row">
                        <div className="col-xs-12">
                            <div className="pull-sm-left store-home"><a href="http://www.aftership.com"
                                                                        className="store-home--text">AfterShip</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

var Footer = React.createClass({
    render: function () {
        return (
                <div className="row m-y-3">
                    <div className="col-md-6 text-xs-center text-md-left text-muted">
                        <ul className="ui-list">
                            <li className="powered-by-aftership">Powered by <a
                                href="https://www.aftership.com">AfterShip</a>
                            </li>
                            <li><a href="https://www.aftership.com/terms" className="link--muted">Terms</a></li>
                            <li><a href="https://www.aftership.com/privacy" className="link--muted">Privacy</a></li>
                        </ul>
                    </div>
                </div>
        )
    }
});


var Welcome2 = React.createClass({
    render: function () {
        return (
            <div className="page-content-wrapper text-09">
                <div className="container-fluid">
                    <div className="row title-row">
                        <div className="col-xs-12">
                            <div className="pull-sm-left store-home"><a href="http://www.aftership.com"
                                                                        className="store-home--text">AfterShip</a>
                            </div>
                        </div>
                    </div>
                    <div className="block m-b-2">
                        <div className="row">
                            <div className="col-xs-12"><p id="tracking-number"
                                                          className="tracking-number--bar text-xs-center m-b-0">
                                1ZY8V5520457704777</p></div>
                            <div className="col-xs-12">
                                <div className="col-xs-12 courier-info media m-y-1">
                                    <div className="media-left"><a href="https://www.aftership.com/courier/ups">
                                        <img src={'//assets.aftership.com/couriers/svg/ups.svg'} width="64"
                                             height="64"/>
                                    </a>
                                    </div>
                                    <div className="media-right"><a href="https://www.aftership.com/courier/ups"
                                                                    className="link--black"><h2
                                        className="h4 notranslate">UPS</h2></a><a
                                        href="tel:1800834834" className="link--phone">1800834834</a></div>
                                </div>
                            </div>
                            <div className="col-xs-12">
                                <div className="clearfix text-xs-center tag-delivered additional-info">
                                    <div className="col-sm-6"><p className="tag text-tight">Delivered</p></div>
                                    <div className="col-sm-6"><p className="text-tight">Signed by: BEN</p></div>
                                </div>
                            </div>
                            <div className="col-xs-12">
                                <div className="checkpoints">
                                    <ul className="checkpoints__list">
                                        <li className="checkpoint">
                                            <div className="checkpoint__time"><strong>Jul 19, 2016</strong>
                                                <div className="hint">03:00 pm</div>
                                            </div>
                                            <div className="checkpoint__icon delivered"></div>
                                            <div className="checkpoint__content"><strong>Delivered<span
                                                className="checkpoint__courier-name">UPS</span></strong>
                                                <div className="hint">GIVATAYIM, IL, 53401</div>
                                            </div>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={Welcome1}/>
        <Route path="/:parcelId" component={Welcome2}/>
    </Router>
), document.getElementById('page'));

ReactDOM.render((
    <Footer></Footer>
), document.getElementById('footer'));
