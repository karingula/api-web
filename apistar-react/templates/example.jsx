var MyComponent = React.createClass({
    render: function(){
        return(
            <h2> Hello world!</h2>
        );
    }
});

ReactDOM.render(
    <MyComponent/>, document.getElementById("content")
)