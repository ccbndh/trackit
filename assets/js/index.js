var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory

var Welcome = React.createClass({
    render: function () {
        return (
            <h1>
                Tracking your parcel!
            </h1>
        )
    }
});

var InputForm = React.createClass({
    getInitialState: function () {
        return {parcelId: ''};
    },
    handleParcelIdChange: function (e) {
        this.setState({parcelId: e.target.value});
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var parcelId = this.state.parcelId.trim();
        if (!parcelId) {
            return;
        }
        // TODO: send request to the server
        this.setState({parcelId: ''});
    },
    render: function () {
        return (
            <form className="input-group" onSubmit={this.handleSubmit}>
                <input
                    type="text"
                    placeholder="Enter your parcel id"
                    value={this.state.parcelId}
                    onChange={this.handleParcelIdChange}
                />
                <input type="submit" value="Track"/>
            </form>
        );
    }
});


var Home = React.createClass({
    render: function () {
        return (
            <div>
                <Welcome />
                <InputForm />
            </div>
        )
    }
});


var Tracking = React.createClass({
    render: function () {
        return (<h1>Tracking result: {this.props.params.parcelId}</h1>);
    }
});

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={Home}/>
        <Route path="/:parcelId" component={Tracking}/>
    </Router>

), document.getElementById('container'));
