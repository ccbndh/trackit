var React = require('react');

var Footer = React.createClass({
    render: function () {
        return (
                <div className="row m-y-3">
                    <div className="col-md-6 text-xs-center text-md-left text-muted">
                        <ul className="ui-list">
                            <li className="powered-by-trackit">Powered by <a
                                href="">Trackit         </a>
                            </li>
                            <li><a href="" className="link--muted">Terms</a></li>
                            <li><a href="" className="link--muted">Privacy</a></li>
                        </ul>
                    </div>
                </div>
        )
    }
});

module.exports = Footer;