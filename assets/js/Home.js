var React = require('react');

var Home = React.createClass({
    render: function () {
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
                </div>
            </div>
        )
    }
});

module.exports = Home;