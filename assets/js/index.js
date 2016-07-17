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

        $.ajax({
            url: "http://127.0.0.1:8000/api/v1/task/",
            dataType: 'json',
            type: 'POST',
            data: {"parcel_id": parcelId},
            success: function (resTask) {
                (function poll() {
                    $.ajax({
                        url: "http://127.0.0.1:8000/api/v1/task/?task_id=" + resTask.task_id,
                        type: "GET",
                        success: function (resData) {
                            console.log(resData)
                        }, dataType: "json", error: poll, timeout: 30000
                    });
                })();
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
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
