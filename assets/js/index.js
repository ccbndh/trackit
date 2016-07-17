var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory

var Home = React.createClass({
	render: function() {
		return (
			<h1>
			Tracking your parcel!
			</h1>
		)
	}
});

var Tracking = React.createClass({
  render: function() {
     return (<h1>Tracking result: {this.props.params.parcelId}</h1>);
  }
});

ReactDOM.render((
  <Router history={browserHistory}>
      <Route path="/" component={Home} />
      <Route path="/:parcelId" component={Tracking} />
  </Router>

), document.getElementById('container'));