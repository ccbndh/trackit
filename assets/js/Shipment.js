var React = require('react');

var Shipment = React.createClass({
    render: function () {
        this.props.params.parcelId = this.props.params.parcelId.trim().toUpperCase();
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
                    <div className="block m-b-2">
                        <div className="row">
                            <div className="col-xs-12"><p id="tracking-number"
                                                          className="tracking-number--bar text-xs-center m-b-0">
                                {this.props.params.parcelId}</p></div>
                            <div className="col-xs-12">
                                <div className="col-xs-12 courier-info media m-y-1">
                                    <div className="media-left"><a href="">
                                        <img src={'//assets.aftership.com/couriers/svg/ups.svg'} width="64"
                                             height="64"/>
                                    </a>
                                    </div>
                                    <div className="media-right"><a href=""
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

module.exports = Shipment;