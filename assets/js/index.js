var React = require('react');
var ReactDOM = require('react-dom');
var Router = require('react-router').Router
var Route = require('react-router').Route
var Link = require('react-router').Link
var browserHistory = require('react-router').browserHistory
var Config = require('Config')

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
        this.setState({parcelId: e.target.value.trim().toUpperCase()});
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var parcelId = this.state.parcelId.trim();
        if (!parcelId) {
            return;
        }

        $.ajax({
            url: Config.serverUrl + "/api/v1/task/",
            dataType: 'json',
            type: 'POST',
            data: {"parcel_id": parcelId},
            success: function (task) {
                (function poll() {
                    $.ajax({
                        url: Config.serverUrl + "/api/v1/task/?task_id=" + task.task_id,
                        type: "GET",
                        success: function (events) {
                            console.log(events);
                            ReactDOM.render(
                                <EventList events={events}/>,
                                document.getElementById('container-events')
                            );
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
            <form className="form-inline" onSubmit={this.handleSubmit}>
                <input
                    className="form-control"
                    type="text"
                    placeholder="Enter your parcel id"
                    value={this.state.parcelId}
                    onChange={this.handleParcelIdChange}
                />
                <input className="btn btn-primary" type="submit" value="Track"/>
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


var EventList = React.createClass({
    render: function () {
        var events = this.props.events;
        return (
            <div className="events">
                {
                    events.map(function (event, i) {
                        return (
                            <div key={i}
                                className="event-detail">{event.event_name} {event.event_localtion} {event.event_time}</div>
                        );
                    })
                }
            </div>
        );
    }
});

ReactDOM.render((
    <Router history={browserHistory}>
        <Route path="/" component={Home}/>
    </Router>

), document.getElementById('container'));
