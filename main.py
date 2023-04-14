from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from ontology_dc8f06af066e4a7880a5938933236037 import nlp, context
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    # TODO Add code here
    for text in request.text:
        response = nlp(question=text, context=context)
        output.append(response["answer"])

    return SimpleText(dict(text=output))
