from plugins.outputs.ca_apm_rest import metricBatch

def process_line(line):
    
    metricBasePath = 'LogMetrics|%(process)s|%(host)s|%(port)s|%(element_name)s' % line
    
    mb = metricBatch() 

    mb.addMetric('IntCounter', metricBasePath + ':LAST',line["LAST"])
    mb.addMetric('IntCounter', metricBasePath + ':LOW', line["LOW"])
    mb.addMetric('IntCounter', metricBasePath + ':HIGH',line["HIGH"])
    mb.sendMetrics(False)