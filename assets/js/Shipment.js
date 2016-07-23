var React = require('react');
var ReactDOM = require('react-dom');
var Config = require('Config');

var ShipmentNotFound = React.createClass({
    render: function () {
        return (
            <div className="page-content-wrapper text-09">
                <div className="container-fluid">
                    <div className="row title-row">
                        <div className="col-xs-12">
                            <div className="pull-sm-left store-home">
                                We can't track your parcel
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

var EventListDetail = React.createClass({
    render: function () {
        var events = this.props.events;
        return (
            <div className="checkpoints">
                <ul id="events" className="checkpoints__list">
                    {
                        events.map(function (event, i) {
                            return (
                                <li key={i} className="checkpoint">
                                    <div className="checkpoint__time"><strong>{event.event_time}</strong>
                                        <div className="hint"></div>
                                    </div>
                                    <div className="checkpoint__icon delivered"></div>
                                    <div className="checkpoint__content"><strong>{event.event_name}</strong>
                                        <div className="hint">{event.event_location}</div>
                                    </div>
                                </li>
                            );
                        })
                    }
                </ul>
            </div>
        );
    }
});

var ShipmentDetail = React.createClass({
    render: function () {
        var events = this.props.events;
        var parcel = events[0].parcel;
        var carrier = events[0].carrier;
        var latestEvent = events[0];
        document.title = Config.mainTitle + " - " + carrier.name + " - " + parcel.parcel_id;
        var logoCarrier = '//assets.aftership.com/couriers/svg/' + carrier.slug_name + '.svg';
        return (
            <div className="row">
                <div className="col-xs-12"><p id="tracking-number"
                                              className="tracking-number--bar text-xs-center m-b-0">
                    {parcel.parcel_id}</p></div>
                <div className="col-xs-12">
                    <div className="col-xs-12 courier-info media m-y-1">
                        <div className="media-left"><a href="">
                            <img src={logoCarrier} width="64"
                                 height="64"/>
                        </a>
                        </div>
                        <div className="media-right"><a href=""
                                                        className="link--black"><h2
                            className="h4 notranslate">{carrier.name}</h2></a><a
                            href={"tel:" + carrier.carrier_cs_phone} className="link--phone">{carrier.carrier_cs_phone}</a></div>
                    </div>
                </div>
                <div className="col-xs-12">
                    <div className="clearfix text-xs-center tag-delivered additional-info">
                        <div className="col-sm-6"><p className="tag text-tight">{parcel.status}</p></div>
                        <div className="col-sm-6"><p className="text-tight">{latestEvent.event_name}</p></div>
                    </div>
                </div>
                <div className="col-xs-12">
                    <EventListDetail events={events}/>
                </div>
            </div>
        )
    }
});

var Shipment = React.createClass({
    render: function () {
        var parcelId = this.props.params.parcelId.trim().toUpperCase();
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
                        dataType: "json",
                        success: function (events) {
                            if(events.length > 0) {
                                ReactDOM.render(
                                    <ShipmentDetail events={events}/>,
                                    document.getElementById('shipment')
                                );
                            }else{
                                ReactDOM.render(
                                    <ShipmentNotFound events={events}/>,
                                    document.getElementById('shipment')
                                );
                            }
                        }, error: function (event) {
                            setTimeout(poll, 2000);
                        }
                    });
                })();
            }.bind(this),
            error: function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });

        return (
            <div className="page-content-wrapper text-09">
                <div className="container-fluid">
                    <div className="row title-row">
                        <div className="col-xs-12">
                            <div className="pull-sm-left store-home"><a href=""
                                                                        className="store-home--text">Trackit</a>
                            </div>
                        </div>
                    </div>
                    <div id="shipment" className="block m-b-2">

                    </div>
                </div>
            </div>
        )
    }
});

module.exports = Shipment;
