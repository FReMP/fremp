import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
    };
  }

  async getData() {
    await fetch('/api/get/')
      .then(response => response.json())
      .then(json => {
        console.log(json)
        this.setState({
          data: json,
        })
      })
  }

  componentDidMount() {
    this.getData()
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <div>
            <h1>{this.state.data.data}</h1>
          </div>
        </header>
      </div>
    );
  }
}

export default App;
