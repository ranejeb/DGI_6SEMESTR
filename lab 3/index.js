const V = [1, 1, 1, 0, 0, 0, 0];

const vectors = [];

for (let i = 0; i < 7; i++) {
  vectors.push(V.slice(i).concat(V.slice(0, i)));
}

vectors.push([0, 0, 0, 0, 0, 0, 0]);

let resultVectors = [];

for (let item of vectors) {
  resultVectors.push(item.join(""));
}

for (let i = 0; i < vectors.length; i++) {
  for (let j = i; j < vectors.length; j++) {
    const sumVector = new Array(7);

    for (let k = 0; k < vectors[i].length; k++) {
      sumVector[k] = (vectors[i][k] + vectors[j][k]) % 2;
    }

    if (!resultVectors.includes(sumVector.join(""))) {
      resultVectors.push(sumVector.join(""));
    }
  }
}

resultVectors = resultVectors.map((item) => item.split(""));

resultVectors = resultVectors.map((array) => array.map((item) => +item));

resultVectors.push([1, 1, 1, 1, 1, 1, 1]);

for (let item of resultVectors) {
  console.log(item.toString());
}

console.log(resultVectors.length);

const sum = (a,b) =>{
    const tmp = new Array(b.length)
    for(let i=0;i<a.length;i++){
        tmp[i]=(a[i]+b[i])%2
    }
    return tmp
}

//Минимальное кодовое расстояние
let minDist = 999

for(let i=0;i<resultVectors.length-1;i++){
    for(let j=i+1;j<resultVectors.length;j++){
        const p=sum(resultVectors[i],resultVectors[j])
        let dist = 0
        for(let k=0; k<7;k++){
            dist=dist+p[k]
        }
        if(dist<minDist){
            minDist = dist
        }
    }
}

console.log('minDist', minDist)

//Синдромы
//python