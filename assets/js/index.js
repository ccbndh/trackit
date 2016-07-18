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
        this.setState({parcelId: e.target.value.trim().toUpperCase()});
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
                            console.log(resData);

                            ReactDOM.render(
                                <Parcel parcel={resData.parcel}/>,
                                document.getElementById('container-parcel')
                            );

                            ReactDOM.render(
                                <Carrier carrier={resData.carrier}/>,
                                document.getElementById('container-carrier')
                            );

                            ReactDOM.render(
                                <EventList events={resData.events_details}/>,
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



var Parcel = React.createClass({
    render: function () {
        var parcel = this.props.parcel;
        return (
            <div className="parcel">
               {parcel.parcel_id} {parcel.status} {parcel.size} {parcel.weight}
            </div>
        );
    }
});


var Carrier = React.createClass({
    render: function () {
        var carrier = this.props.carrier;
        return (
            <div className="carrier">
               {carrier.slug_name}
            </div>
        );
    }
});

var EventList = React.createClass({
    render: function () {
        var events = this.props.events;
        return (
            <div className="events">
                {
                    events.map(function (event) {
                        return (
                            <div
                                className="event-info">{event.event_name} {event.event_localtion} {event.event_time}</div>
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
