const BASE_URL = "http://127.0.0.1:5000/api";
const DEFALUT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"



/** given data about a cupcake, generate html */

function generateCupcakeHTML(cupcake) {
  return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="${cupcake.flavor} cupcake">
      </div>
    `;
}


/** put initial cupcakes on page. */

async function showInitialCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);

  for (let cupcakeData of response.data.cupcakes) {
    let newCupcake = $(generateCupcakeHTML(cupcakeData));
    $("#cupcakes-list").append(newCupcake);
  }
}


/** handle form for adding of new cupcakes */

async function handleFormSubmit(evt){
  evt.preventDefault();

  let flavor = $("#form-flavor").val();
  let rating = $("#form-rating").val();
  let size = $("#form-size").val();
  let image = $("#form-image").val() || DEFALUT_IMAGE_URL;


  const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, 
                                              {flavor, rating, size, image});

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#new-cupcake-form").trigger("reset");

}

$("#new-cupcake-form").on("submit", handleFormSubmit);


/** handle clicking delete: delete cupcake */

$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
 
  let $cupcake = $(evt.target).closest("div");
  console.log ($cupcake)
  // let cupcakeId = $cupcake.attr("data-cupcake-id");
  let cupcakeId = $cupcake.data ('cupcake-id');
  
  console.log (`the id is ${cupcakeId}`);

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();

});


$(showInitialCupcakes);