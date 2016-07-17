var React = require('react');
var ReactDOM = require('react-dom');

var Hello = React.createClass({
	render: function() {
		return (
			<h1>
			Tracking your parcel!
			</h1>
		)
	}
});

var CommentForm = React.createClass({
  render: function() {
    return (
      <form className="commentForm">
        <input type="text" placeholder="Enter parcel id" />
        <input type="submit" value="Track" />
      </form>
    );
  }
});

ReactDOM.render(<Hello />, document.getElementById('container-welcome'))
ReactDOM.render(<CommentForm />, document.getElementById('container-form'))
