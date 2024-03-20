/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package thrift

import (
	"context"
)

// upgradeProtocolFactory is a ProtocolFactory for a protocol that upgrades from Header to Rocket protocol.
type upgradeToRocketProtocolFactory struct{}

// NewUpgradeToRocketProtocolFactory creates a new upgradeProtocolFactory that upgrades from Header to Rocket protocol.
func NewUpgradeToRocketProtocolFactory() protocolFactory {
	return &upgradeToRocketProtocolFactory{}
}

func (p *upgradeToRocketProtocolFactory) GetProtocol(trans Transport) Protocol {
	return NewUpgradeToRocketProtocol(trans)
}

type upgradeToRocketProtocol struct {
	Protocol
	rocketProtocol Protocol
	headerProtocol Protocol
}

// NewUpgradeToRocketProtocol creates a protocol that upgrades from Header to Rocket protocol from a transport.
func NewUpgradeToRocketProtocol(trans Transport) Protocol {
	return &upgradeToRocketProtocol{
		rocketProtocol: NewRocketProtocol(trans),
		headerProtocol: NewHeaderProtocol(trans),
	}
}

// NewUpgradeToRocketProtocol creates a protocol that upgrades from Header to Rocket protocol given both protocols.
func NewUpgradeToRocketProtocols(rocketProtocol, headerProtocol Protocol) Protocol {
	return &upgradeToRocketProtocol{
		rocketProtocol: rocketProtocol,
		headerProtocol: headerProtocol,
	}
}

// WriteMessageBegin first sends a upgradeToRocket message using the HeaderProtocol.
// If this succeeds, we switch to the RocketProtocol and write the message using it.
// If this fails, we send the original message using the HeaderProtocol and continue using the HeaderProtocol.
func (p *upgradeToRocketProtocol) WriteMessageBegin(name string, typeID MessageType, seqid int32) error {
	if p.Protocol == nil {
		if err := p.upgradeToRocket(); err != nil {
			p.Protocol = p.headerProtocol
		} else {
			p.Protocol = p.rocketProtocol
		}
	}
	return p.Protocol.WriteMessageBegin(name, typeID, seqid)
}

func (p *upgradeToRocketProtocol) upgradeToRocket() error {
	return upgradeToRocket(context.Background(), p.headerProtocol)
}

func (p *upgradeToRocketProtocol) SetPersistentHeader(key, value string) {
	if p.Protocol == nil {
		p.rocketProtocol.SetPersistentHeader(key, value)
		p.headerProtocol.SetPersistentHeader(key, value)
		return
	}
	p.Protocol.SetPersistentHeader(key, value)
}

func (p *upgradeToRocketProtocol) GetPersistentHeader(key string) (string, bool) {
	v, ok := p.GetPersistentHeaders()[key]
	return v, ok
}

func (p *upgradeToRocketProtocol) GetPersistentHeaders() map[string]string {
	if p.Protocol == nil {
		headers := p.headerProtocol.GetPersistentHeaders()
		rocketHeaders := p.rocketProtocol.GetPersistentHeaders()
		for k, v := range rocketHeaders {
			headers[k] = v
		}
		return headers
	}
	return p.Protocol.GetPersistentHeaders()
}

func (p *upgradeToRocketProtocol) ClearPersistentHeaders() {
	if p.Protocol == nil {
		p.rocketProtocol.ClearPersistentHeaders()
		p.headerProtocol.ClearPersistentHeaders()
		return
	}
	p.Protocol.ClearPersistentHeaders()
}

func (p *upgradeToRocketProtocol) SetRequestHeader(key, value string) {
	if p.Protocol == nil {
		p.rocketProtocol.(RequestHeaders).SetRequestHeader(key, value)
		p.headerProtocol.(RequestHeaders).SetRequestHeader(key, value)
		return
	}
	p.Protocol.(RequestHeaders).SetRequestHeader(key, value)
}

func (p *upgradeToRocketProtocol) GetRequestHeader(key string) (value string, ok bool) {
	v, ok := p.GetRequestHeaders()[key]
	return v, ok
}

func (p *upgradeToRocketProtocol) GetRequestHeaders() map[string]string {
	if p.Protocol == nil {
		headers := p.headerProtocol.(RequestHeaders).GetRequestHeaders()
		rocketHeaders := p.rocketProtocol.(RequestHeaders).GetRequestHeaders()
		for k, v := range rocketHeaders {
			headers[k] = v
		}
		return headers
	}
	return p.Protocol.(RequestHeaders).GetRequestHeaders()
}

func (p *upgradeToRocketProtocol) GetResponseHeader(key string) (string, bool) {
	v, ok := p.GetResponseHeaders()[key]
	return v, ok
}

func (p *upgradeToRocketProtocol) GetResponseHeaders() map[string]string {
	if p.Protocol == nil {
		headers := p.headerProtocol.GetResponseHeaders()
		rocketHeaders := p.rocketProtocol.GetResponseHeaders()
		for k, v := range rocketHeaders {
			headers[k] = v
		}
		return headers
	}
	return p.Protocol.GetResponseHeaders()
}
