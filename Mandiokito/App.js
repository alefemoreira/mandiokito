/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow
 */

import React, {Component} from 'react';
import {
  SafeAreaView,
  StyleSheet,
  ScrollView,
  View,
  Text,
  TextInput,
  TouchableOpacity,
  StatusBar,
} from 'react-native';

import {
  Header,
  LearnMoreLinks,
  Colors,
  DebugInstructions,
  ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';

class App extends Component{
  constructor(props){
    super(props);
    this.state = {altura:0, massa:0, resultado:0,resultadoText:""}
    this.calcular = this.calcular.bind(this)
  };
  calcular(){
    let s = this.state;
    let imc = s.massa/(s.altura*s.altura);
    s.resultado = imc;
    
    if (s.resultado < 16) {
      s.resultadoText = "Magreza Grave";
    } else if (s.resultado < 17) {
      s.resultadoText = "Magreza Moderada";
    } else if (s.resultado <18.5) {
      s.resultadoText = "Magreza Leve";
    } else if (s.resultado <25) {
      s.resultadoText = "Saudável";
    }  else if (s.resultado < 30) {
      s.resultadoText = "Sobre Peso";
    } else if (s.resultado < 35) {
      s.resultadoText = "Obesidade Grau I";
    } else if (s.resultado < 40) {
      s.resultadoText = "Obesidade Grau II";
    } else {
      s.resultadoText = "Obesidade Grau III";
    }

    this.setState(s);
  };
  render(){
    return (
      <View style={styles.container}>
          <TouchableOpacity style={styles.button} onPress={this.calcular}><Text style={styles.buttonText}>Registrar</Text></TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={this.calcular}><Text style={styles.buttonText}>Apagar</Text></TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={this.calcular}><Text style={styles.buttonText}>Atualizar</Text></TouchableOpacity>
      </View>
    );
  };
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5FCFF',
  },
  entradas: {
    flexDirection: 'row'
  },
  input: {
    height:80,
    textAlign:'center',
    width:"50%",
    fontSize:50,
    marginTop:24,
    color:"gray",
  },
  button: {
    backgroundColor: '#89FFA5',
  },
  buttonText: {
    alignSelf: 'center',
    padding: 30,
    fontSize:25,
    color: '#6DC4A4',
    fontWeight:'bold',
  },
  resultado: {
    alignSelf: 'center',
    color:"lightgray",
    fontSize:65,
    padding:15
  }
});

export default App;

