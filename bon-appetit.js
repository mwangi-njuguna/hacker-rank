function bonAppetit(bill, k, b) {
    const getArraySum = arr => arr.reduce((acc, curr) => acc + curr, 0);

    const exemptedAmount = bill[k];
    const fairAmount = getArraySum(bill) - exemptedAmount;
    const amountPerIndividual = fairAmount/2;

    const result = b !== amountPerIndividual ? b - amountPerIndividual : "Bon Appetit";

    console.log(result);
}