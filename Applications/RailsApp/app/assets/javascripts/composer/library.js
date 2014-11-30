	function Library(){
		this.preload();
		this.init();
	};

	Library.prototype = {
		init: function(){
			var self = this;
			Library.set_actuators();
		},
		preload: function(){
			api.count("flavors");
			api.count("actuators");
		},
		get_selected: function(){
			return {
				actuator: Library.find_selected("#actuator-list"),
				flavor: Library.find_selected("#flavor-list"),
				behavior: Library.find_selected("#behavior-list")
			}
		}
	}
		Library.find_selected = function(list){
			el = $(list).find('.selected2, .selected').children();
			return  el.length > 0 ? parseInt(el.attr('data-id')) : undefined;
		}
		Library.set_flavors = function(actuator_id){
			var self = this;	
			if(actuator_id == this.current_actuator) return;
			
			this.current_actuator = actuator_id;
			
			$('#flavor-list table').html('');
			$('#behavior-list table').html('');
			this.current_flavor = undefined;
			api.get_flavors(actuator_id, function(data){
				$('#flavor-list table').append(Library.listify(data, true, Library.set_behaviors, "flavors"));
			});
		}
		Library.set_actuators = function(){
			var self = this;			
			$('#actuator-list table').html('');
			api.get_actuators(function(data){
				$('#actuator-list table').append(Library.listify(data, true, Library.set_flavors, "actuators"));
			});	
		}
		Library.set_behaviors = function(flavor_id){
			var self = this;			
			if(flavor_id == this.current_flavor) return;
			
			this.current_flavor = flavor_id;
			$('#behavior-list table').html('');
			api.get_behaviors(flavor_id, function(data){
				$('#behavior-list table').append(Library.listify(data, false, Library.set_wave, null));
			});	
		}
		Library.set_wave = function(behavior_id){
			if(behavior_id == this.current_behavior) return;
			this.current_behavior = behavior_id;
		}

	Library.selected = function(el){
		$('.selected2').removeClass('selected2').addClass('selected');
		$(el).parent().addClass('selected2').siblings().removeClass('selected selected2')
	}

	Library.listify = function(els, with_decor, get, type){
		return $.map(els, function(el, i){
			// If no <next_order_semantic>  found, disable the caller;
			var count = type ? "(" + api.count(type)[el.id] + ")" : "";
			var nullify = count  == "(undefined)";
			var count = nullify ? "" : count;

			var play = DOM.tag("span").addClass("glyphicon glyphicon-play").attr("aria-hidden","true");
			var decoration = DOM.tag("td").addClass('decoration-right').attr('data-id', el.id).html(play);
			var name = DOM.tag("td").addClass('noselect')
									.attr('data-id', el.id)
									.html(el.name + " "+ count)
									.click(function(){
										var id = parseInt($(this).attr('data-id'));
										get(id);
										Library.selected(this);
									});

			if(nullify) name.addClass("disabled").unbind("click");
			return with_decor && !nullify ? DOM.tag("tr").html([name, decoration]) : DOM.tag("tr").html(name);
		});
	} 