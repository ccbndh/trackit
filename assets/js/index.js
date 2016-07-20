var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router;
var Route = require('react-router').Route;
var browserHistory = require('react-router').browserHistory
var Config = require('Config');
var Home = require('./Home');
var Shipment = require('./Shipment');
var Footer = require('./Footer');

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={Home}/>
        <Route path="/:parcelId" component={Shipment}/>
    </Router>
), document.getElementById('page'));

ReactDOM.render((
    <Footer></Footer>
), document.getElementById('footer'));
