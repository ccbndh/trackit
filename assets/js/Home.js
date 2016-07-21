var React = require('react');
var Router = require('react-router').Router;
var transitionTo = Router.transitionTo;

var Home = React.createClass({
    getInitialState: function () {
        return {parcelId: ''};
    },
    handleParcelIdChange: function (e) {
        this.setState({parcelId: e.target.value});
    },
    handleSubmit: function (e) {
        e.preventDefault();
        var parcelId = this.state.parcelId.trim().toUpperCase();
        if (!parcelId) {
            return;
        }
        this.setState({parcelId: ''});
        location.href = parcelId;
    },

    render: function () {
        return (
            <div className="page-content-wrapper text-09">
                <div className="container-fluid">
                    <div className="row title-row">
                        <div className="col-xs-12">
                            <div className="pull-sm-left store-home"><a href=""
                                                                        className="store-home--text">Track order
                                status</a>
                                <form className="tracking-widget -responsive" onSubmit={this.handleSubmit}>
                                    <div className="tracking-widget-ui">
                                        <input type="text" className="text-large text-input"
                                               placeholder="Tracking Number" value={this.state.parcelId}
                                               onChange={this.handleParcelIdChange}/>
                                        <button value="submit" type="submit" className="btn"
                                        >
                                            <span className="btn__text">Track</span>
                                        </button>
                                    </div>
                                </form>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

module.exports = Home;